import drone.common as common
from djitellopy import Tello

from drone.utils.go_to_pad import go_to_pad


def around(tello: Tello):
    times = common.config['around']
    for _i in range(times):
        if common.padId in range(1, 9):
            if common.change:
                go_to_pad(common.padId)
        print(f"Going around.")
        tello.move_right(common.config['around_x'])
        tello.move_forward(common.config['around_y'])
        tello.move_left(common.config['around_x'])
