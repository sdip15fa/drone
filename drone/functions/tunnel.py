from djitellopy_reduced import Tello


def tunnel(tello: Tello) -> None:
    while tello.get_distance_tof() > 30:
        try:
            tello.move_down(20)
        except:
            break
