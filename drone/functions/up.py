from djitellopy_reduced import Tello
import drone.common as common

runs: int = 0


def up(tello: Tello):
    global runs

    change_init = common.config['up_change'][runs] if runs < len(common.config['up_change']) else common.config['up_change_default']
    height = common.config["up_height"][runs] if runs < len(common.config["up_height"]) else common.config["up_height_default"]

    print(f"move up {height}cm")

    tello.move_up(height)

    if change_init:
        common.config["init_height"] += height
        common.height_changed = True
        
    common.executed = True
    runs += 1
