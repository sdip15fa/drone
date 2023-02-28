from djitellopy_reduced import Tello
import drone.common as common
from drone.utils.detect_obs_height import detect_obs_height

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

    obs_height = detect_obs_height(tello, max_height, max_distance)

    tello.go_xyz_speed_mid(
        0, 0, (obs_height - 15 if obs_height - 15 >= 20 else 20) if obs_height else init_height, common.config['speed'], common.running)

    if not obs_height:
        return common.running

    runs += 1
