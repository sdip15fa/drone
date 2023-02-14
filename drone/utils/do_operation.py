import drone.common as common
from time import sleep
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
from drone.functions.go_through_predefined_heights import go_through_predefined_heights
from drone.functions.tunnel import tunnel
from drone.functions.snake import snake
from drone.functions.rotate import rotate


def do_operation(pad: int) -> None:
    """
    The do_operation function is the main function of the program. It takes in a
    pad number and executes all of the functions that are associated with that pad
    number. The do_operation function also checks to see if there is a change in 
    the config file, and if so, it will update its values.
    
    :param pad: int: Determine which pad to go to
    :return: None
    :doc-author: Trelent
    """
    common.config = get_config()

    if pad in range(1, 9):
        if common.change:
            # sleep(5)
            go_to_pad(pad)
    else:
        pad = 1

    while pad:
        pad = match_functions(pad)


def match_functions(pad: int) -> int:
    """
    The match_functions function is a switch statement that matches the current mode to the corresponding function.
    The match_functions function also handles switching between modes and pads.
    
    :param pad: int: the pad id
    :return: the next pad id to be run, otherwise 0
    :doc-author: Trelent
    """
    run_pad: int = 0
    match common.config['mode']:
        case 1:
            match pad:
                case 1:
                    run_pad = execute(forward, False)
                case 2:
                    run_pad = execute(back, False)
                case 3:
                    run_pad = execute(left, False)
                case 4:
                    run_pad = execute(right, False)
                case 5:
                    run_pad = execute(up, True)
                case 6:
                    run_pad = execute(down, True)
                case 7:
                    run_pad = execute(around, True)
                    # rerun_pad = execute(circle, True)
                case 8:
                    if common.config['switch_mode']:
                        common.config['mode'] = 2
                        common.config['switch_mode'] -= 1
                        common.mode_switched = True
                        common.pads_permanent = [
                            1, 2, 4] if common.config['mode'] == 2 else list(range(1, 5))
                    else:
                        run_pad = execute(land, True)
        case 2:
            match pad:
                case 1:
                    run_pad = execute(forward, False)
                case 2:
                    # rerun_pad = execute(back, False)
                    run_pad = execute(tunnel, True)
                case 3:
                    run_pad = execute(left, False)
                case 4:
                    run_pad = execute(right, False)
                case 5:
                    run_pad = execute(go_through, True)
                    # rerun_pad = execute(go_through_predefined_heights, True)
                case 6:
                    run_pad = execute(rotate, True)
                case 7:
                    run_pad = execute(around, True)
                case 8:
                    if common.config['switch_mode']:
                        common.config['mode'] = 1
                        common.config['switch_mode'] -= 1
                        common.mode_switched = True
                        common.pads_permanent = [
                            1, 2, 4] if common.config['mode'] == 2 else list(range(1, 5))
                    else:
                        run_pad = execute(land, True)
    return run_pad
