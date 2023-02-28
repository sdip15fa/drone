import drone.common as common
from djitellopy_reduced import Tello


def back(tello: Tello):
    print(f"move back {common.config['distance']}cm")
    tello.move_back(common.config["distance"])
    common.direction = 2
