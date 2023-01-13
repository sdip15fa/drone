from djitellopy import Tello
import drone.common as common
from drone.utils.detect_obs_height import detect_obs_height
import type_enforced


@type_enforced.Enforcer
def go_through(tello: Tello) -> None:
    obs_height = detect_obs_height(tello)
    if not obs_height:
        return
    common.prev = 1
