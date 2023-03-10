from djitellopy_reduced import Tello
import drone.common as common

runs: int = 0


def up(tello: Tello):
    global runs

    height = common.config["up_height"][runs] if runs < len(common.config["up_height"]) else common.config["up_height_default"]

    print(f"move up {height}cm")

    tello.move_up(height)

    common.executed = True
    runs += 1
