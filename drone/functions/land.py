from djitellopy_reduced import Tello
import drone.common as common


def land(tello: Tello):
    print("land")
    tello.land()
    common.end = True
    common.executed = True
