from djitellopy import Tello
from lib import set_interval
from dotenv import load_dotenv
import os

load_dotenv()

prev = None
padId = -1

executed = False
end = False
change = True


def getConfig() -> dict[str, str | int]:
    return {
        'height': int(os.getenv('HEIGHT') or 100) or 100,
        'around': int(os.getenv('AROUND') or 1) or 1,
        'ip': os.getenv('TELLO_IP') or "192.168.10.1",
        'speed': int(os.getenv('SPEED') or 60) or 60,
        'distance': int(os.getenv('DISTANCE') or 30) or 30,
    }

config = getConfig()

def main(tello: Tello = Tello(host=config["ip"])) -> None:
    global prev, padId, executed, end, change

    # wait until connection is established
    tello.connect(True)
    print("Tello connected")

    sdk = tello.query_sdk_version()
    print(f"SDK version: {sdk}")
    battery = tello.get_battery()
    print(f"battery: {battery}%")

    print("enabling mission pads detection")
    tello.enable_mission_pads()

    padId = tello.get_mission_pad_id()
    print(f"mission pad id: {padId}")

    print("Taking off")
    tello.takeoff()
    print("Took off")

    tello.set_speed(config["speed"])

    if not tello.is_flying:
        print("Tello not flying")
        return

    height = tello.get_height()

    if height < config["height"]:
        print(f"Moving up to {config['height']}cm")
        tello.move_up(config["height"] - height)

    def onChange() -> None:
        global executed, change
        executed = False
        change = True

    def updatePadId() -> None:
        global end, prev, padId
        if end:
            return
        newPadId = tello.get_mission_pad_id()
        if (newPadId in range(1, 9) and padId != newPadId):
            prev = padId
            padId = newPadId
            print("new pad id", padId)
            onChange()

    def monitor() -> dict[str, int]:
        height = tello.get_height()
        print(f"height: {height} cm")
        battery = tello.get_battery()
        print(f"battery: {battery}%")
        temp = tello.get_temperature()
        print(f"temperature: {temp} °C")
        tof = tello.get_distance_tof()
        print(f"tof distance: {tof} cm")
        return {"height": height, "battery": battery, "temperature": temp, "tof": tof}

    updatePadInterval = set_interval(updatePadId, 500)
    monitorInterval = set_interval(monitor, 2000)

    def do_operation(pad: int) -> None:
        global executed, end, change

        config = getConfig()

        if pad in range(1, 9):
            if change:
                print(f"go to mission pad {pad}")
                tello.go_xyz_speed_mid(
                    0, 0, config["height"], config["speed"], pad)
                change = False
        else:
            pad = 1
        match pad:
            case 1:
                print(f"move forward {config['distance']}cm")
                tello.move_forward(config["distance"])
            case 2:
                print(f"move back {config['distance']}cm")
                tello.move_back(config["distance"])
            case 3:
                print(f"move left {config['distance']}cm")
                tello.move_left(config["distance"])
            case 4:
                print(f"move right {config['distance']}cm")
                tello.move_right(config["distance"])
            case 5:
                if not executed:
                    print(f"move up {config['distance']}cm")
                    tello.move_up(config["distance"])
                    config["height"] += config["distance"]
                    executed = True
                else:
                    do_operation(prev if prev in range(1, 5) else 1)
            case 6:
                if not executed:
                    print(f"move down {config['distance']}cm")
                    tello.move_down(config["distance"])
                    config["height"] -= config["distance"]
                    executed = True
                else:
                    do_operation(prev if prev in range(1, 5) else 1)
            case 7:
                if not executed:
                    times = config['around']
                    while times:
                        if pad in range(1, 9):
                            if change:
                                print(f"go to mission pad {pad}")
                                tello.go_xyz_speed_mid(
                                    0, 0, config["height"], config["speed"], pad)
                                change = False
                        tello.move_right(70)
                        tello.move_forward(150)
                        tello.move_left(70)
                        times -= 1
                    executed = True
                else:
                    do_operation(prev if prev in range(1, 5) else 1)
            case 8:
                if not executed:
                    print("land")
                    tello.land()
                    end = True
                    executed = True

    while True:
        if end:
            updatePadInterval.cancel()
            monitorInterval.cancel()
            exit(0)
        else:
            do_operation(padId)
