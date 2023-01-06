import drone.common as common
from typing import Callable
import drone.utils.do_operation as do


def execute(func: Callable, once: bool) -> None:
    if common.end:
        return
    if once:
        if not common.executed:
            func(common.tello)
            common.executed = True
        else:
            do.do_operation(common.prev if common.prev in range(1, 5) else 1)
    else:
        func(common.tello)