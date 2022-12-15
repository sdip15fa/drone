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


def main(tello: Tello = Tello(host=os.getenv("TELLO_IP") or "192.168.10.1")):
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

    tello.set_speed(60)

    print(tello.get_height())

    if tello.get_height() < 50:
        print("height less that 50cm, moving up 30cm")
        tello.move_up(30)

    if not tello.is_flying:
        print("Tello not flying")
        return

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

    updatePadInterval=set_interval(updatePadId, 500)
    monitorInterval=set_interval(monitor, 2000)

    def do_operation(pad: int) -> None:
        global executed, end, change
        if pad in range(1, 9):
            if change:
                print(f"go to mission pad {pad}")
                tello.go_xyz_speed_mid(0, 0, 100, 60, pad)
                change = False
        else:
            pad=1
        match pad:
            case 1:
                print("move forward 30cm")
                tello.move_forward(30)
            case 2:
                print("move back 30cm")
                tello.move_back(30)
            case 3:
                print("move left 30cm")
                tello.move_left(30)
            case 4:
                print("move right 30cm")
                tello.move_right(30)
            case 5:
                if not executed:
                    print("move up 30cm")
                    tello.move_up(30)
                    executed=True
                else:
                    do_operation(prev if prev in range(1, 5) else 1)
            case 6:
                if not executed:
                    print("move down 30cm")
                    tello.move_down(30)
                    executed=True
                else:
                    do_operation(prev if prev in range(1, 5) else 1)
            case 7:
                if not executed:
                    times = int(os.environ["AROUND"]) if os.environ["AROUND"] else 1
                    while times:
                        times -= 1
                        tello.move_right(70)
                        tello.move_forward(150)
                        tello.move_left(70)
                    executed = True
                else:
                    do_operation(prev if prev in range(1, 5) else 1)
            case 8:
                if not executed:
                    print("land")
                    tello.land()
                    end=True
                    executed=True

    while True:
        if end:
            updatePadInterval.cancel()
            monitorInterval.cancel()
            exit(0)
        else:
            do_operation(padId)
