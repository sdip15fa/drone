from dotenv import load_dotenv
import os


def get_config() -> dict[str, str | int]:
    load_dotenv()

    try:
        import common
    except:
        common = None
        
    return {
        'init_height': int(os.getenv('INIT_HEIGHT') or 100) or 100,
        'height': int(os.getenv('HEIGHT') or 100) or 100,
        'around': int(os.getenv('AROUND') or 1) or 1,
        'around_x': int(os.getenv('AROUND_X') or 60) or 60,
        'around_y': int(os.getenv('AROUND_Y') or 100) or 100,
        'circle': int(os.getenv('CIRCLE') or 1) or 1,
        'circle_x': int(os.getenv('CIRCLE_X') or 60) or 60,
        'circle_y': int(os.getenv('CIRCLE_Y') or 100) or 100,
        'rotate': int(os.getenv('ROTATE') or 6) or 6,
        'ip': os.getenv('TELLO_IP') or "192.168.10.1",
        'speed': int(os.getenv('SPEEDD') or 60) or 60,
        'distance': int(os.getenv('DISTANCE') or 30) or 30,
        'min_height': int(os.getenv('MIN_HEIGHT') or 30) or 30,
        'max_height': int(os.getenv('MAX_HEIGHT') or 200) or 200,
        'min_distance': int(os.getenv('MIN_DISTANCE') or 30) or 30,
        'mode': common.config['mode'] if common and common.mode_switched else int(os.getenv('MODE') or 1) or 1,
        'switch_mode': common.config['switch_mode'] if common and common.mode_switched else int(os.getenv('SWITCH_MODE') or 0) or 0,
    }
