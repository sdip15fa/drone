from djitellopy_reduced import Tello
from typing import Callable

from drone.utils.get_config import get_config

config = get_config()

tello: Tello = Tello(host=config["ip"])

prev: int = 0
padId: int = -1
running: int = -1
detected: int = -1
executed: bool = False
end: bool = False
change: bool = False

mode_switched: bool = False
height_changed: bool = False

pads_permanent: list[int] = [
    1, 2, 4] if config['mode'] == 2 else list(range(1, 5))

direction: int = config['direction_default'] or 1


def directions_funcs(dir: int) -> Callable:
    """
    The directions function is a decorator that takes an integer as input.
    The integer corresponds to the direction in which the drone will move.
    The directions are defined by their index in a list of functions:
        [move_forward, move_back, move_left, move_right]

    :param dir: int: Determine which direction the drone will move in
    :return: A function that can be called using the tello object
    :doc-author: Trelent
    """
    functions = [tello.move_forward, tello.move_back,
                 tello.move_left, tello.move_right]
    func = functions[dir - 1 if dir - 1 < len(function) else 0]
    return func
