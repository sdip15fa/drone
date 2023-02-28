from threading import Timer
from djitellopy_reduced import Tello
import drone.common as common

from drone.lib import set_interval

obs_height: int = None
tof: int = 0


def get_tof() -> None:
    """
    The get_tof function is a function that gets the distance tof from the Tello.
    It also checks if it is less than max_height - 40 and returns if true.
    
    :return: The distance from the tello to the ground
    :doc-author: Trelent
    """
    global tof
    try:
        # if tof <= common.config['max_height'] - 40:
        #    return
        tof = common.tello.get_distance_tof()
        print(f"current tof distance: {tof}")
    except Exception as e:
        print(e)


def detect_obs_height(tello: Tello, max_height: int, max_distance: int) -> int:
    """
    The detect_obs_height function is used to detect the height of an obstacle.
    If height is detected, the drone stays at ~20cm lower than the height, and the function returns the height.
    If not, it returns None.
    
    :param tello: Tello: Access the tello object
    :param max_height: int: Set the maximum height of the drone
    :param max_distance: int: Limit the distance that the drone will fly
    :return: The height of an obstacle
    :doc-author: Trelent
    """
    global obs_height, tof
    # original_height = tello.get_distance_tof()

    tello.go_xyz_speed_mid(
        0, 0, max_height, common.config['speed'], common.running)

    init_height = tello.get_height()
    tof = tello.get_distance_tof()
    init_tof = tof
    
    tello.set_speed(10)

    tof_interval: Timer = set_interval(get_tof, 100)

    flew_distance: int = 0

    while flew_distance < max_distance:
        if tof <= init_tof - (max_height / 4):
            height = init_tof - tof
            print(f"height: {height}")
            tof_interval.cancel()
            return height
        common.directions_funcs(common.direction)(20)
        flew_distance += 20
    
    return None
