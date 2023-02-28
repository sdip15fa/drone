from djitellopy_reduced import Tello
import drone.common as common



def forward(tello: Tello) -> None:
    print(f"move forward {common.config['distance']}cm")
    tello.move_forward(common.config["distance"])
    common.direction = 1
