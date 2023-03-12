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
    times = range(common.config["rotate_times"][runs] if runs < len(
        common.config["rotate_times"]) else common.config["rotate_times_default"])

    print(f"Rotating {times} times")

    if times > 6:
        for _ in 12 - times:
            tello.rotate_counter_clockwise(30)
    else:
        for _ in times:
            tello.rotate_clockwise(30)

    common.executed = True
    runs += 1
