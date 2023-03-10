from djitellopy_reduced import Tello
from drone.utils.get_config import get_config

config = get_config()

tello: Tello = Tello(host=config["ip"])

prev: int = 0
padId: int = -1
running: int = -1
lastrun: int = -1
detected: int = -1
executed: bool = False
end: bool = False
change: bool = False

mode_switched: bool = False

pads_permanent: list[int] = [
    1, 2, 4] if config['mode'] == 2 else list(range(1, 5))

direction: int = config['direction_default'] or 1
height: int = config['height_default'] or 100
