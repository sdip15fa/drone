from djitellopy_reduced import Tello
import drone.common as common

times = 0


# use pre-defined obstacle heights
def go_through_predefined_heights(tello: Tello) -> None:
    global times
    heights = common.config['obs_height']
    tello.go_xyz_speed_mid(0, 0, heights[times if times < len(
        heights) else -1] - 30, common.config['speed'], common.padId)
    times += 1
