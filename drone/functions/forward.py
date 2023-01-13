from djitellopy import Tello
import drone.common as common
import type_enforced

@type_enforced.Enforcer
def forward(tello: Tello) -> None:
    print(f"move forward {common.config['distance']}cm")
    tello.move_forward(common.config["distance"])
