from djitellopy_reduced import Tello
import drone.common as common




def tunnel(tello: Tello) -> None:
    # tello.go_xyz_speed(0, 0, 30, common.config["speed"])
    while tello.get_distance_tof() > 30:
        try:
            tello.move_down(20)
        except:
            break
    common.prev = common.prev if common.prev in range(1, 5) else 1
