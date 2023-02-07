from djitellopy_reduced import Tello
import drone.common as common

runs = 0


def rotate(tello: Tello) -> None:
    global runs
    times = common.config["rotate_times"]
    for _ in range(times[runs] if runs < len(times) else common.config["rotate_times_default"]):
        tello.rotate_clockwise(30)
    runs += 1
