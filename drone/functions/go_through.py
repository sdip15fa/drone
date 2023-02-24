from djitellopy_reduced import Tello
import drone.common as common
from drone.utils.detect_obs_height import detect_obs_height

runs: int = 0


def go_through(tello: Tello) -> None:
    global runs
    common.prev = (common.config['go_through_change_prev'][runs] if runs < len(common.config['go_through_change_prev'])
                   else common.config['go_through_change_prev_default']) or common.prev
    init_height = tello.get_height()
    max_height = common.config['go_through_max_height'][runs] if runs < len(common.config['go_through_max_height']) \
        else common.config['go_through_max_height_default']
    max_distance = common.config['go_through_max_distance'][runs] if runs < len(common.config['go_through_max_distance']) \
        else common.config['go_through_max_distance_default']
    obs_height = detect_obs_height(tello, max_height, max_distance)
    tello.go_xyz_speed_mid(
        0, 0, (obs_height - 15 if obs_height - 15 >= 20 else 20) if obs_height else init_height, common.config['speed'], common.running)
    if not obs_height:
        return common.running
    runs += 1
