from djitellopy_reduced import Tello
from typing import Callable

from drone.utils.get_config import get_config
from drone.functions.forward import forward
from drone.functions.back import back
from drone.functions.left import left
from drone.functions.right import right

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
height_changed: bool = False

pads_permanent: list[int] = [
    1, 2, 4] if config['mode'] == 2 else list(range(1, 5))

direction: int = config['direction_default'] or 1

