import drone.common as common
from djitellopy_reduced import Tello

from drone.utils.go_to_pad import go_to_pad

runs = 0

def circle(tello: Tello):
    global runs
    times: list[int] = common.config['circle_times']
    for _ in range(times[runs] if runs < len(times) else common.config['circle_times_default']):
        tello.move_right(common.config['circle_x'])
        tello.move_forward(common.config['circle_y'])
        tello.move_left(2 * common.config['circle_x'])
        tello.move_back(common.config['circle_y'])
        tello.move_right(common.config['circle_x'])
        go_to_pad(common.padId)
    runs += 1
