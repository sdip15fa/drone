from djitellopy import Tello
import drone.common as common
import type_enforced

@type_enforced.Enforcer
def detect_obs_height(tello: Tello) -> int:
    """
    Detects the height of an obstacle.
    If height is detected, the drone stays at ~20cm lower than the height, and the function returns the height.
    If not the drone returns to the original height, and the function returns None.

    :param tello: The Tello object.
    :return: The height of the obstacle.
    """
    obs_height: int = None
    original_height = tello.get_height()
    tello.move_up(common.config["max_height"] - original_height)
    while (tello.get_height() >= common.config["min_height"]):
        tello.move_down(20)
        tof = tello.get_distance_tof()
        print(f"current tof distance: {tof}")
        if tof <= common.config["min_distance"]:
            while tof <= common.config["min_distance"]:
                obs_height = tello.get_height()
                tello.move_down(20)
            break
    tello.move_up(original_height - tello.get_height())
    return obs_height