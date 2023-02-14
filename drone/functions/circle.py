import drone.common as common
from djitellopy_reduced import Tello

from drone.utils.go_to_pad import go_to_pad

runs = 0

def circle(tello: Tello):
    global runs
    times: list[int] = common.config['circle_times']
    x_distance = common.config['circle_x'][runs] if runs < len(common.config['circle_x']) else common.config['circle_x_default']
    y_distance = common.config['circle_y'][runs] if runs < len(common.config['circle_y']) else common.config['circle_y_default']
    for _ in range(times[runs] if runs < len(times) else common.config['circle_times_default']):
        tello.move_right(x_distance)
        tello.move_forward(y_distance)
        tello.move_left(2 * x_distance)
        tello.move_back(y_distance)
        tello.move_right(x_distance)
        go_to_pad(common.padId)
    runs += 1
