from typing import Callable
import drone.common as common
from drone.functions.forward import forward
from drone.functions.back import back
from drone.functions.left import left
from drone.functions.right import right

def directions_funcs(dir: int, exec: bool = False) -> Callable:
    """
    The directions function is a decorator that takes an integer as input.
    The integer corresponds to the direction in which the drone will move.
    The directions are defined by their index in a list of functions:
        [move_forward, move_back, move_left, move_right]

    :param dir: int: Determine which direction the drone will move in
    :return: A function that can be called using the common.tello object
    :doc-author: Trelent
    """
    functions = [forward, back, left, right] if exec else [common.tello.move_forward, common.tello.move_back,
                 common.tello.move_left, common.tello.move_right]
    func = functions[dir - 1 if dir - 1 < len(functions) else 0]
    return func