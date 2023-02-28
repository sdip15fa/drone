import drone.common as common
from typing import Callable


def execute(func: Callable) -> int:
    """
    The execute function is the main function that runs all of the commands.
    It takes in a Callable, which is any class or function that has a __call__ method.
    This allows us to pass in functions and classes as well as single methods. 
    The execute function also takes an optional once parameter, which defaults to False.

    :param func: Callable: Pass the function to be executed
    :param once: bool: Determine whether the function should be executed only once or not
    :return: The mission pad id to be rerun, otherwise 0
    :doc-author: Trelent
    """
    if common.end:
        return 0

    if not common.executed:
        run_pad = func(common.tello)
        common.executed = True
        return run_pad
    else:
        common.directions_funcs(common.direction or 1)        
        return 0
