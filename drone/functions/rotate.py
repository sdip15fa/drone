from djitellopy_reduced import Tello
import drone.common as common

runs = 0


def rotate(tello: Tello) -> None:
    """
    The rotate function tells the drone to rotate clockwise 30 degrees.
    It does this a number of times, as specified in the config file.
    
    :param tello: Tello: Access the tello object
    :return: None
    :doc-author: Trelent
    """
    global runs
    times = common.config["rotate_times"]
    for _ in range(times[runs] if runs < len(times) else common.config["rotate_times_default"]):
        tello.rotate_clockwise(30)
    common.executed = True
    runs += 1
