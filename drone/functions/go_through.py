from djitellopy_reduced import Tello
import drone.common as common
from drone.utils.detect_obs_height import detect_obs_height


def go_through(tello: Tello) -> None:
    obs_height = detect_obs_height(tello)
    if not obs_height:
        return
    tello.go_xyz_speed_mid(
        0, 0, obs_height - 30 if obs_height - 30 >= 20 else 20, common.config['speed'], common.padId)
