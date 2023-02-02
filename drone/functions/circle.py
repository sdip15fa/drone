import drone.common as common
from djitellopy import Tello

from drone.utils.go_to_pad import go_to_pad


def circle(tello: Tello):
    # tello.curve_xyz_speed(0, 0, 0, 0, 100, 0, common.config["speed"])
    for _i in range(common.config['circle']):
        tello.move_right(common.config['circle_x'])
        tello.move_forward(common.config['circle_y'])
        tello.move_left(2 * common.config['circle_x'])
        tello.move_back(common.config['circle_y'])
        tello.move_right(common.config['circle_x'])
        go_to_pad(common.padId)
