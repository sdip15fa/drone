from djitellopy import Tello
import drone.common as common

def rotate(tello: Tello) -> None:
    for _i in range(common.config["rotate"]):
        tello.rotate_clockwise(30)
