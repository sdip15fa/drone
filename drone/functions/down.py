from djitellopy_reduced import Tello
import drone.common as common

runs: int = 0


def down(tello: Tello):
    global runs

    change_init = common.config['down_change'][runs] if runs < len(common.config['down_change']) else common.config['down_change_default']
    height = common.config["down_height"][runs] if runs < len(common.config["down_height"]) else common.config["down_height_default"]

    print(f"move down {height}cm")

    tello.move_down(height)

    if change_init:
        common.config["init_height"] += height
        common.height_changed = True
        
    common.executed = True
    runs += 1
