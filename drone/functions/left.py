import drone.common as common
from djitellopy_reduced import Tello


def left(tello: Tello):
    print(f"move left {common.config['distance']}cm")
    tello.move_left(common.config["distance"])
    common.executed = True
    # common.direction = 3