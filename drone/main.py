from djitellopy import Tello
from lib import set_interval
from utils import goToPad
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

pref = None
padId = -1

executed = False
wait = False
end = False


def main(tello: Tello = Tello(host=os.getenv("TELLO_IP") or "192.168.10.1")):
    global pref, padId, executed, wait, end

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

    tello.move_up(30)

    if not tello.is_flying:
        print("Tello not flying")
        return

    def onChange() -> None:
        global wait, executed
        wait = True
        executed = False
        goToPad(tello)
        wait = False

    def updatePadId() -> None:
        global prev, padId, wait
        newPadId = tello.get_mission_pad_id()
        if (newPadId not in range(1, 9)):
            pass
        elif (padId != newPadId):
            while wait:
                sleep(0.1)
            prev = padId
            padId = newPadId
            print("new pad id", padId)
            wait = True
            onChange()
            wait = False

    def monitor() -> dict[str, int]:
        height = tello.get_height()
        print(f"height: {height} cm")
        battery = tello.get_battery()
        print(f"battery: {battery}%")
        temp = tello.get_temperature()
        print(f"temperature: {temp} °C")
        return {"height": height}

    set_interval(updatePadId, 500)
    set_interval(monitor, 5000)

    def do_operation(pad: int):
        global executed, end, wait
        if wait:
            sleep(0.1)
            return
        if pad not in range(1, 9):
            pad = 1
        # print("executed", executed)
        match pad:
            case 1:
                print("move forward 50cm")
                wait = True
                tello.move_forward(50)
                wait = False
            case 2:
                print("move back 50cm")
                wait = True
                tello.move_back(50)
                wait = False
            case 3:
                print("move left 20cm")
                wait = True
                tello.move_left(50)
                wait = False
            case 4:
                print("move right 20cm")
                wait = True
                tello.move_right(50)
                wait = False
            case 5:
                if not executed:
                    print("move up 50cm")
                    wait = True
                    tello.move_up(50)
                    wait = False
                    executed = True
                else:
                    do_operation(prev if prev in range(1, 5) else 1)
            case 6:
                if not executed:
                    print("move down 50cm")
                    wait = True
                    tello.move_down(50)
                    wait = False
                    executed = True
                else:
                    do_operation(prev if prev in range(1, 5) else 1)
            case 7:
                if not executed:
                    print("curve to (0, 100, 0) via (50, 50, 0)")
                    wait = True
                    tello.curve_xyz_speed(0, 100, 0, -50, 50, 0, 50)
                    wait = False
                    executed = True
                else:
                    do_operation(prev if prev in range(1, 5) else 1)
            case 8:
                if not executed:
                    print("land")
                    wait = True
                    tello.land()
                    end = True
                    executed = True
                    return exit(0)

    while True:
        if end:
            break
        do_operation(padId)
