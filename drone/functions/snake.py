from djitellopy_reduced import Tello
import drone.common as common
def snake(tello: Tello) -> None:
    tello.move_right(common.config["around_x"])
    tello.move_forward(common.config["around_y"])
    tello.move_left(common.config["around_x"] * 2)
    tello.move_forward(common.config["around_y"])
    tello.move_right(common.config["around_x"])
