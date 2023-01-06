from dotenv import load_dotenv
import os


def get_config() -> dict[str, str | int]:
    load_dotenv()
    return {
        'init_height': int(os.getenv('INIT_HEIGHT') or 100) or 100,
        'height': int(os.getenv('HEIGHT') or 100) or 100,
        'around': int(os.getenv('AROUND') or 1) or 1,
        'around_x': int(os.getenv('AROUND_X') or 60) or 60,
        'around_y': int(os.getenv('AROUND_Y') or 100) or 100,
        'ip': os.getenv('TELLO_IP') or "192.168.10.1",
        'speed': int(os.getenv('SPEEDD') or 60) or 60,
        'distance': int(os.getenv('DISTANCE') or 30) or 30,
    }
