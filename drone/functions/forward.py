from djitellopy import Tello
import drone.common as common
import type_enforced

@type_enforced.Enforcer
def forward(tello: Tello) -> None:
    if (tello.get_distance_tof() < common.config['distance']):
        print(f"TOF distance is less than {common.config['distance']}cm, refusing to move forward.")
        return
    print(f"move forward {common.config['distance']}cm")
    tello.move_forward(common.config["distance"])
