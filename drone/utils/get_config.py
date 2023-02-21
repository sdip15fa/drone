from dotenv import load_dotenv
import os


def get_config() -> dict[str, str | int | list[int]]:
    """
    The get_config function returns a dictionary of configuration values.
    The get_config function is used to retrieve the current configuration values from the environment variables.
    
    
    :return: A dictionary of configuration values
    :doc-author: Trelent
    """
    load_dotenv()

    try:
        import common
    except:
        common = None

    
    return {
        'init_height': common.config['init_height'] if common and common.height_changed else int(os.getenv('INIT_HEIGHT') or 100) or 100,
        'height': int(os.getenv('HEIGHT') or 100) or 100,
        'around_times': eval(os.getenv('AROUND_TIMES') or '[]') or [],
        'around_times_default': int(os.getenv('AROUND_TIMES_DEFAULT') or 1) or 1,
        'around_x': eval(os.getenv('AROUND_X') or '[]') or [],
        'around_y': eval(os.getenv('AROUND_Y') or '[]') or [],
        'around_x_default': int(os.getenv('AROUND_X_DEFAULT') or 60) or 60,
        'around_y_default': int(os.getenv('AROUND_Y_DEFAULT') or 100) or 100,
        'circle_times': eval(os.getenv('CIRCLE_TIMES') or '[]') or [],
        'circle_times_default': int(os.getenv('CIRCLE_TIMES_DEFAULT') or 1) or 1,
        'circle_x': eval(os.getenv('CIRCLE_X') or '[]') or [],
        'circle_y': eval(os.getenv('CIRCLE_Y') or '[]') or [],
        'circle_x_default': int(os.getenv('CIRCLE_X_DEFAULT') or 60) or 60,
        'circle_y_default': int(os.getenv('CIRCLE_Y_DEFAULT') or 100) or 100,
        'rotate_times': eval(os.getenv('ROTATE_TIMES') or '[]') or [],
        'rotate_times_default': int(os.getenv('ROTATE_TIMES_DEFAULT') or 6) or 6,
        'ip': os.getenv('TELLO_IP') or "192.168.10.1",
        'speed': int(os.getenv('SPEEDD') or 60) or 60,
        'distance': int(os.getenv('DISTANCE') or 30) or 30,
        'mode': common.config['mode'] if common and common.mode_switched else int(os.getenv('MODE') or 1) or 1,
        'obs_height': eval(os.getenv('OBS_HEIGHT') or '[100]') or [100],
        'obs_height_default': int(os.getenv('OBS_HEIGHT_DEFAULT') or 100) or 100,
        'switch_mode': common.config['switch_mode'] if common and common.mode_switched else int(os.getenv('SWITCH_MODE') or 0) or 0,
        'tunnel_change_prev': eval(os.getenv('TUNNEL_CHANGE_PREV') or '[]') or [],
        'tunnel_change_prev_default': int(os.getenv('TUNNEL_CHANGE_PREV_DEFAULT') or 0) or 0,
        'go_through_max_height': eval(os.getenv('GO_THROUGH_MAX_HEIGHT') or '[]') or [],
        'go_through_max_height_default': int(os.getenv('GO_THROUGH_MAX_HEIGHT_DEFAULT') or 200) or 200,
        'go_through_change_prev': eval(os.getenv('GO_THROUGH_CHANGE_PREV') or '[]') or [],
        'go_through_change_prev_default': int(os.getenv('GO_THROUGH_CHANGE_PREV_DEFAULT') or 0) or 0,
        'go_through_max_distance': eval(os.getenv('GO_THROUGH_MAX_DISTANCE') or '[]') or [],
        'go_through_max_distance_default': int(os.getenv('GO_THROUGH_MAX_DISTANCE_DEFAULT') or 100) or 100,
        'blacklist_repeat_pads': eval(os.getenv('BLACKLIST_REPEAT_PADS') or '[]') or []
    }
