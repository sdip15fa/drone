import drone.common as common
from djitellopy_reduced import Tello


def right(tello: Tello):
    print(f"move right {common.config['distance']}cm")
    tello.move_right(common.config["distance"])
    common.direction = 4
