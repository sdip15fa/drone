import drone.common as common
from djitellopy_reduced import Tello

from drone.utils.go_to_pad import go_to_pad

runs = 0


def around(tello: Tello):
    global runs
    times: list[int] = common.config['around_times']
    for i in range(times[runs] if runs < len(times) else common.config['around_times_default']):
        if common.padId in range(1, 9):
            if common.change:
                go_to_pad(common.padId)
        print(f"Going around.")
        if i % 2 == 0:
            tello.move_right(common.config['around_x'])
            tello.move_forward(common.config['around_y'])
            tello.move_left(common.config['around_x'])
        else:
            tello.move_left(common.config['around_x'])
            tello.move_forward(common.config['around_y'])
            tello.move_right(common.config['around_x'])
    runs += 1
