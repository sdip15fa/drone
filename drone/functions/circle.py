import drone.common as common
from drone.utils.directions_funcs import directions_funcs
from djitellopy_reduced import Tello

from drone.utils.go_to_pad import go_to_pad
from drone.utils.dir_relative import dir_back, dir_left, dir_right

runs = 0


def circle(tello: Tello):
    global runs
    times: list[int] = common.config['circle_times']
    x_distance = common.config['circle_x'][runs] if runs < len(
        common.config['circle_x']) else common.config['circle_x_default']
    y_distance = common.config['circle_y'][runs] if runs < len(
        common.config['circle_y']) else common.config['circle_y_default']
    for _ in range(times[runs] if runs < len(times) else common.config['circle_times_default']):
        directions_funcs(dir_right(common.direction))(x_distance)
        directions_funcs(common.direction)(y_distance)
        directions_funcs(dir_left(common.direction))(2 * x_distance)
        directions_funcs(dir_back(common.direction))(y_distance)
        directions_funcs(dir_right(common.direction))(x_distance)
        go_to_pad(common.padId)
    common.executed = True
    runs += 1
