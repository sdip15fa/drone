from djitellopy_reduced import Tello
import drone.common as common

runs: int = 0


def down(tello: Tello):
    global runs

    height = common.config["down_height"][runs] if runs < len(common.config["down_height"]) else common.config["down_height_default"]

    print(f"move down {height}cm")

    tello.move_down(height)

    common.executed = True
    runs += 1
