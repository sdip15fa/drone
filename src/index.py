import djitellopy
from lib import set_interval
from utils import goToPad
from time import sleep

tello = djitellopy.Tello()

# wait until connection is established
tello.connect(True)
print("Tello connected")

tello.enable_mission_pads()
tello.takeoff()

pref = None
padId = tello.get_mission_pad_id()

executed = False
wait = False


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


set_interval(updatePadId, 100)


def do_operation(pad: int):
    global executed
    if wait:
        sleep(0.1)
    if pad not in range(1, 9):
        return None
    match pad:
        case 1:
            tello.move_forward(20)
        case 2:
            tello.move_back(20)
        case 3:
            tello.move_left(20)
        case 4:
            tello.move_right(20)
        case 5:
            if not executed:
                tello.move_up(50)
            else:
                do_operation(prev if prev in range(1, 5) else 1)
        case 6:
            if not executed:
                tello.move_down(50)
            else:
                do_operation(prev if prev in range(1, 5) else 1)
        case 7:
            tello.curve_xyz_speed
        case 8:
            if not executed:
                tello.land()
    executed = True


while True:
    do_operation(padId)
