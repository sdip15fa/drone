from threading import Timer
from djitellopy import Tello
import drone.common as common
import type_enforced
from drone.lib import set_interval

obs_height: int = None
tof: int = 0

@type_enforced.Enforcer
def get_tof() -> None:
    global tof
    try:
        if tof <= common.config['max_height'] - 40:
            return
        tof = common.tello.get_distance_tof()
        print(f"current tof distance: {tof}")
    except Exception as e:
        print(e)


@type_enforced.Enforcer
def detect_obs_height(tello: Tello) -> int:
    """
    Detects the height of an obstacle.
    If height is detected, the drone stays at ~20cm lower than the height, and the function returns the height.
    If not the drone returns to the original height, and the function returns None.

    :param tello: The Tello object.
    :return: The height of the obstacle.
    """
    global obs_height, tof
    #original_height = tello.get_distance_tof()

    tello.go_xyz_speed_mid(
        0, 0, common.config['max_height'], common.config['speed'], 5)
    init_height = tello.get_height()
    tof = tello.get_distance_tof()
    init_tof = tof
    tello.set_speed(10)
    tof_interval: Timer = set_interval(get_tof, 100)
    while (tello.get_height() >= common.config["min_height"]):
        if tof <= init_tof - 50:
            print(f"height: {init_tof - tof}")
            tof_interval.cancel()
            break
        tello.move_forward(20)
    tof_interval.cancel()
    tello.go_xyz_speed_mid(
        0, 0, init_height, common.config['speed'], common.padId)
    tello.move_down(tof)
    return tof
