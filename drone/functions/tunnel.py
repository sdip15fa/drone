from djitellopy_reduced import Tello
import drone.common as common

runs = 0


def tunnel(tello: Tello) -> None:
    global runs
    change_prev = common.config['tunnel_change_prev']
    while tello.get_distance_tof() > 40:
        try:
            tello.move_down(20)
        except:
            break
    common.prev = (change_prev[runs] if runs < len(change_prev)
                   else common.config['tunnel_change_prev_default']) or common.prev
    runs += 1
