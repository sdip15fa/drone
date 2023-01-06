from djitellopy import Tello
import drone.common as common


def forward(tello: Tello) -> None:
    print(f"move forward {common.config['distance']}cm")
    tello.move_forward(common.config["distance"])
