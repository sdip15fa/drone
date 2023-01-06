import drone.common as common
from djitellopy import Tello


def right(tello: Tello):
    print(f"move right {common.config['distance']}cm")
    tello.move_right(common.config["distance"])
