from djitellopy import Tello
import drone.common as common




def tunnel(tello: Tello) -> None:
    # tello.go_xyz_speed(0, 0, 30, common.config["speed"])
    while tello.get_distance_tof() > 40:
        tello.move_down(20)
    common.prev = 1
