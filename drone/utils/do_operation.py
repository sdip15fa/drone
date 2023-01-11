import drone.common as common
from drone.utils.get_config import get_config
from drone.utils.go_to_pad import go_to_pad
from drone.utils.execute import execute

# functions
from drone.functions.forward import forward
from drone.functions.back import back
from drone.functions.left import left
from drone.functions.right import right
from drone.functions.up import up
from drone.functions.down import down
from drone.functions.around import around
from drone.functions.circle import circle
from drone.functions.land import land
from drone.functions.go_through import go_through

import type_enforced

@type_enforced.Enforcer
def do_operation(pad: int) -> None:
    common.config = get_config()

    if pad in range(1, 9):
        if common.change:
            go_to_pad(pad)
    else:
        pad = 1

    match common.config['mode']:
        case 1:
            match pad:
                case 1:
                    execute(forward, False)
                case 2:
                    execute(back, False)
                case 3:
                    execute(left, False)
                case 4:
                    execute(right, False)
                case 5:
                    execute(up, True)
                case 6:
                    execute(down, True)
                case 7:
                    execute(around, True)
                    # execute(circle, True)
                case 8:
                    execute(land, True)
        case 2:
            match pad:
                case 1:
                    execute(forward, False)
                case 2:
                    execute(back, False)
                case 3:
                    execute(left, False)
                case 4:
                    execute(right, False)
                case 5:
                    execute(go_through, True)
                case 6:
                    execute(circle, True)
                case 7:
                    execute(around, True)
                case 8:
                    execute(land, True)