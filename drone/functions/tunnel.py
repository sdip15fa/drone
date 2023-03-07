from time import sleep
from djitellopy_reduced import Tello
import drone.common as common

from drone.utils.dir_relative import dir_back, dir_left, dir_right
from drone.utils.go_to_pad import go_to_pad
from drone.utils.directions_funcs import directions_funcs

runs: int = 0


def tunnel(tello: Tello) -> None:
    global runs

    print("tunnel")

    back_mode = common.config['tunnel_back'][runs] if runs < len(
        common.config['tunnel_back']) else 0
    x_distance = common.config['tunnel_x_distance'][runs] if runs < len(
        common.config['tunnel_x_distance']) else common.config['tunnel_x_distance_default']
    y_distance = common.config['tunnel_y_distance'][runs] if runs < len(
        common.config['tunnel_y_distance']) else common.config['tunnel_y_distance_default']
    height = common.config['tunnel_height'][runs] if runs < len(
        common.config['tunnel_height']) else common.config['tunnel_height_default']

    print("tunnel height", tello.query_distance_tof())
    tello.go_xyz_speed_mid(0, 0, 30, 20, common.running)

    if back_mode:
        directions_funcs(common.direction)(y_distance)

        match back_mode:
            case 0:
                pass
            case 1:
                # from left
                directions_funcs(dir_left(common.direction))(x_distance)
            case 2:
                # from right
                directions_funcs(
                    dir_right(common.direction))(x_distance)
            case 3:
                # from up
                tello.move_up(height + 20)
        
        sleep(1)
        directions_funcs(dir_back(common.direction))(y_distance)
        sleep(1)
        go_to_pad(common.running)
        sleep(1)
        tello.go_xyz_speed_mid(0, 0, 30, 20, common.running)

    sleep(1)
    directions_funcs(common.direction)(y_distance)
    tello.move_up(common.config['height'])

    runs += 1
    common.executed = True
