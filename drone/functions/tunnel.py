from djitellopy import Tello
import drone.common as common
import type_enforced


@type_enforced.Enforcer
def tunnel(tello: Tello) -> None:
    tello.go_xyz_speed(0, 0, 30, common.config["speed"])
    common.prev = 1
