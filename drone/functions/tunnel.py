from djitellopy_reduced import Tello
import drone.common as common

from drone.utils.dir_relative import dir_back, dir_left, dir_right
from drone.utils.go_to_pad import go_to_pad

runs: int = 0


def tunnel(tello: Tello) -> None:
    global runs

    back_mode = common.config['tunnel_back'][runs] if runs < len(
        common.config['tunnel_back']) else 0
    x_distance = common.config['tunnel_x_distance'][runs] if runs < len(
        common.config['tunnel_x_distance']) else common.config['tunnel_x_distance_default']
    y_distance = common.config['tunnel_y_distance'][runs] if runs < len(
        common.config['tunnel_y_distance']) else common.config['tunnel_y_distance_default']
    height = common.config['tunnel_height'][runs] if runs < len(
        common.config['tunnel_height']) else common.config['tunnel_height_default']

    while tello.get_height() > 20:
        try:
            tello.move_down(20)
        except:
            break

    if back_mode:
        common.directions_funcs(common.direction)(y_distance)

        match back_mode:
            case 0:
                pass
            case 1:
                # from left
                common.directions_funcs(dir_left(common.direction))(x_distance)
            case 2:
                # from right
                common.directions_funcs(
                    dir_right(common.direction))(x_distance)
            case 3:
                # from up
                tello.move_up(height + 20)

        common.directions_funcs(dir_back(common.direction))(y_distance)
        go_to_pad(common.running)

        while tello.get_height() > 20:
            try:
                tello.move_down(20)
            except:
                break

    common.directions_funcs(common.direction)(y_distance)
    tello.move_up(common.config['height'])

    runs += 1
    common.executed = True
