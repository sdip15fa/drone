from djitellopy_reduced import Tello
import drone.common as common

runs = 0


# use pre-defined obstacle heights
def go_through_predefined_heights(tello: Tello) -> None:
    global runs
    heights: list[int] = common.config['obs_height']
    tello.go_xyz_speed_mid(0, 0, (heights[runs] if runs < len(
        heights) else common.config['obs_height_default']) - 30, common.config['speed'], common.padId)
    runs += 1
