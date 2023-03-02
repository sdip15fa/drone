from djitellopy_reduced import Tello
import drone.common as common


def up(tello: Tello):
    print(f"move up {common.config['height']}cm")
    tello.move_up(common.config["height"])
    common.config["init_height"] += common.config["height"]
    common.height_changed = True
    common.executed = True
    
