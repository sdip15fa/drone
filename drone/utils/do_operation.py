import drone.common as common
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
from drone.functions.land import land


def do_operation(pad: int) -> None:
    common.config = common.get_config()

    pad = go_to_pad(pad)

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
        case 8:
            execute(land, True)