from djitellopy_reduced import Tello
import drone.common as common
from drone.utils.detect_obs_height import detect_obs_height
from drone.utils.dir_relative import dir_back, dir_left, dir_right
from drone.utils.directions_funcs import directions_funcs

runs: int = 0


def go_through(tello: Tello) -> None:
    """
    The go_through function is used to fly the drone through an obstacle.
    It takes in a Tello object and max_height as parameters. It then uses the detect_obs_height function to get the height of
    the obstacle, which it stores in obs_height. If obs_height is None, then there was no obstacle detected and we return running
    to indicate that this function should not be called again until another call to go through has been made by main(). Otherwise,
    we set tello's speed using common.config['speed'], and use goxyzspeedmid() with 0 for xyz coordinates (

    :param tello: Tello: Access the tello instance that is used in this function
    :return: The height of the obstacle that was detected by the detect_obs_height function
    :doc-author: Trelent
    """
    global runs

    init_height = tello.get_height()
    max_height = common.config['go_through_max_height'][runs] if runs < len(common.config['go_through_max_height']) \
        else common.config['go_through_max_height_default']
    max_distance = common.config['go_through_max_distance'][runs] if runs < len(common.config['go_through_max_distance']) \
        else common.config['go_through_max_distance_default']

    mode = (common.config['go_through_mode'][runs] if runs < len(common.config['go_through_mode'])
            else common.config['go_through_mode_default']) or common.config['go_through_mode_default'] or 1

    back = common.config['go_through_back'][runs] if runs < len(common.config['go_through_back']) \
        else common.config['go_through_back_default']

    obs_height: int = 0 if not common.config['go_through_use_predefined'] else ((common.config['go_through_obs_height'][runs] if runs < len(common.config['go_through_obs_height'])
                                                                            else common.config['go_through_obs_height_default']) or common.config['go_through_obs_height_default'])

    obs_y_distance: int = (common.config['go_through_obs_y_distance'][runs] if runs < len(common.config['go_through_obs_y_distance'])
                           else common.config['go_through_obs_y_distance_default']) or common.config['go_through_obs_y_distance_default']
    obs_x_distance: int = (common.config['go_through_obs_x_distance'][runs] if runs < len(common.config['go_through_obs_x_distance'])
                           else common.config['go_through_obs_x_distance_default']) or common.config['go_through_obs_x_distance_default']

    # horizontal mode
    if mode == 1:
        if not common.config['go_through_use_predefined']:
            while not obs_height:
                obs_height = detect_obs_height(tello, max_height, max_distance)
                if not obs_height:
                    tello.go_xyz_speed_mid(
                        0, 0, init_height, common.config['speed'], common.running)
        tello.go_xyz_speed_mid(
            0, 0, (obs_height - 20 if obs_height - 20 >= 20 else 20) if obs_height else init_height, common.config['speed'], common.running)
        directions_funcs(common.direction)(obs_y_distance + 20)
    elif mode == 2:
        tello.go_xyz_speed_mid(
            0, 0, 30, common.config['speed'], common.running)
        directions_funcs(common.direction)(obs_y_distance)
        tello.move_up(obs_height + 30 - tello.query_distance_tof())

    if back:
        match back:
            case 1:
                directions_funcs(dir_left(common.direction))(
                    obs_x_distance + 10)
                directions_funcs(dir_back(common.direction))(
                    obs_y_distance + 10)
                directions_funcs(dir_right(common.direction))(
                    obs_x_distance + 10)
            case 2:
                directions_funcs(dir_right(common.direction))(
                    obs_x_distance + 10)
                directions_funcs(dir_back(common.direction))(
                    obs_y_distance + 10
                )
                directions_funcs(dir_left(common.direction))(
                    obs_x_distance + 10
                )
            case 3:
                if mode == 1:
                    tello.move_up(50)
                directions_funcs(dir_back(common.direction))(
                    obs_y_distance + 10
                )
        if mode == 1:
            tello.go_xyz_speed_mid(
                0, 0, (obs_height - 20 if obs_height - 20 >= 20 else 20) if obs_height else init_height, common.config['speed'], common.running)
            directions_funcs(common.direction)(obs_y_distance + 20)
        elif mode == 2:
            tello.go_xyz_speed_mid(
            0, 0, 30, common.config['speed'], common.running)
            directions_funcs(common.direction)(obs_y_distance)
            tello.move_up(obs_height + 30 - tello.query_distance_tof())

    common.executed = True
    runs += 1
