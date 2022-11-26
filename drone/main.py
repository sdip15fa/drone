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
        global prev, padId
        newPadId = tello.get_mission_pad_id()
        if (padId != newPadId):
            prev = padId
            padId = newPadId
            onChange()
            print("new pad id", padId)

    def monitor() -> dict[str, int]:
        height = tello.get_height()
        print(f"height: {height} cm")
        tello.get_distance_tof
        return {"height": height}

    set_interval(updatePadId, 100)
    set_interval(monitor, 1000)

    def do_operation(pad: int):
        global executed, end
        if wait:
            sleep(0.1)
        if pad not in range(1, 9):
            pad = 1
        match pad:
            case 1:
                print("move forward 20cm")
                tello.move_forward(20)
            case 2:
                print("move back 20cm")
                tello.move_back(20)
            case 3:
                print("move left 20cm")
                tello.move_left(20)
            case 4:
                print("move right 20cm")
                tello.move_right(20)
            case 5:
                if not executed:
                    print("move up 20cm")
                    tello.move_up(50)
                else:
                    do_operation(prev if prev in range(1, 5) else 1)
            case 6:
                if not executed:
                    print("move down 20cm")
                    tello.move_down(50)
                else:
                    do_operation(prev if prev in range(1, 5) else 1)
            case 7:
                if not executed:
                    print("curve to (0, 100, 0) via (25, 50, 0)")
                    tello.curve_xyz_speed(0, 100, 0, 25, 50, 0, 50)
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
            break
        do_operation(padId)
