from time import sleep
import drone.common as common
from drone.utils.directions_funcs import directions_funcs
from djitellopy_reduced import Tello

from drone.utils.go_to_pad import go_to_pad
from drone.utils.dir_relative import dir_back, dir_left, dir_right

runs = 0
around_runs = 0 


def around(tello: Tello):
    global runs, around_runs
    times: list[int] = common.config['around_times']
    circle_times: list[int] = common.config['around_circle_times']
    for i in range(times[runs] if runs < len(times) else common.config['around_times_default']):
        mode = (common.config['around_mode'][around_runs] if around_runs < len(common.config['around_mode']) else common.config['around_mode_default']) or common.config['around_mode_default']

        # may not work
        if common.change and common.padId in range(1, 9):
            go_to_pad(common.padId)
            common.change = False
        
        print(f"Going around.")
        
        x_distance = common.config['around_x'][around_runs] if around_runs < len(common.config['around_x']) else common.config['around_x_default']
        y_distance = common.config['around_y'][around_runs] if around_runs < len(common.config['around_y']) else common.config['around_y_default']

        for _ in range(circle_times[runs] if runs < len(circle_times) else common.config['around_circle_times_default']):
            directions_funcs(dir_right(common.direction))(x_distance)
            directions_funcs(common.direction)(y_distance)
            directions_funcs(dir_left(common.direction))(2 * x_distance)
            directions_funcs(dir_back(common.direction))(y_distance)
            directions_funcs(dir_right(common.direction))(x_distance)
            go_to_pad(common.running)

        if mode == 1:
            directions_funcs(dir_left(common.direction))(x_distance)
            directions_funcs(common.direction)(y_distance)
            directions_funcs(dir_right(common.direction))(x_distance)
        elif mode == 2:
            directions_funcs(dir_right(common.direction))(x_distance)
            directions_funcs(common.direction)(y_distance)
            directions_funcs(dir_left(common.direction))(x_distance)
        elif mode == 3:
            if i % 2 == 0:
                directions_funcs(dir_right(common.direction))(x_distance)
                directions_funcs(common.direction)(y_distance)
                directions_funcs(dir_left(common.direction))(x_distance)
            else:
                directions_funcs(dir_left(common.direction))(x_distance)
                directions_funcs(common.direction)(y_distance)
                directions_funcs(dir_right(common.direction))(x_distance)
        around_runs += 1
    common.executed = True
    runs += 1
