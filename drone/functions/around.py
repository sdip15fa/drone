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
        x_distance = common.config['around_x'][runs] if runs < len(common.config['around_x']) else common.config['around_x_default']
        y_distance = common.config['around_y'][runs] if runs < len(common.config['around_y']) else common.config['around_y_default']
        if i % 2 == 0:
            tello.move_right(x_distance)
            tello.move_forward(y_distance)
            tello.move_left(x_distance)
        else:
            tello.move_left(x_distance)
            tello.move_forward(y_distance)
            tello.move_right(x_distance)
    runs += 1
