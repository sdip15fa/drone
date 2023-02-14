from threading import Timer
from djitellopy_reduced import Tello
import drone.common as common

from drone.lib import set_interval

obs_height: int = None
tof: int = 0


def get_tof() -> None:
    global tof
    try:
        # if tof <= common.config['max_height'] - 40:
        #    return
        tof = common.tello.get_distance_tof()
        print(f"current tof distance: {tof}")
    except Exception as e:
        print(e)


def detect_obs_height(tello: Tello, max_height: int) -> int:
    """
    Detects the height of an obstacle.
    If height is detected, the drone stays at ~20cm lower than the height, and the function returns the height.
    If not the drone returns to the original height, and the function returns None.

    :param tello: The Tello object.
    :return: The height of the obstacle.
    """
    global obs_height, tof
    # original_height = tello.get_distance_tof()

    tello.go_xyz_speed_mid(
        0, 0, max_height, common.config['speed'], 5)
    init_height = tello.get_height()
    tof = tello.get_distance_tof()
    init_tof = tof
    tello.set_speed(10)
    tof_interval: Timer = set_interval(get_tof, 100)
    while True:
        if tof <= init_tof - (common.config["max_height"] / 4):
            height = init_tof - tof
            print(f"height: {height}")
            tof_interval.cancel()
            return height
        {
            1: tello.move_forward,
            2: tello.move_back,
            3: tello.move_left,
            4: tello.move_right,
        }[common.prev if common.prev in common.pads_permanent else 1](20)
