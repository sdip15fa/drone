from djitellopy import Tello
import drone.common as common


def down(tello: Tello):
    print(f"move down {common.config['height']}cm")
    tello.move_down(common.config["height"])
    common.config["init_height"] -= common.config["height"]
    common.executed = True
