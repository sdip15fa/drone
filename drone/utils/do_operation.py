import drone.common as common
from djitellopy_reduced import Tello
from time import sleep
from drone.plugins.update_pad_id import on_change
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
from drone.functions.tunnel import tunnel
from drone.functions.snake import snake
from drone.functions.rotate import rotate

pads = 0


def do_operation(pad: int) -> None:
    global pads
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

    isChange = common.change

    if pad in range(1, 9):
        if common.change:
            # sleep(5)
            on_change()
            go_to_pad(pad)
            common.change = False
    else:
        pad = 1

    while pad:
        common.lastrun = common.running
        common.running = pad
        pad = match_functions(common.config["alias"][pads] if pads < len(
            common.config["alias"]) else pad) or 0
        # sleep(1)
        
    if isChange:
        pads += 1


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
                    run_pad = execute(forward)
                case 2:
                    run_pad = execute(back)
                case 3:
                    run_pad = execute(left)
                case 4:
                    run_pad = execute(right)
                case 5:
                    run_pad = execute(up)
                case 6:
                    run_pad = execute(down)
                case 7:
                    run_pad = execute(around)
                    # run_pad = execute(circle)
                case 8:
                    if common.config['switch_mode']:
                        common.config['mode'] = 2
                        common.config['switch_mode'] -= 1
                        common.mode_switched = True
                        common.pads_permanent = [
                            1, 2, 4] if common.config['mode'] == 2 else list(range(1, 5))
                    else:
                        run_pad = execute(land)
        case 2:
            match pad:
                case 1:
                    # do nothing, just used to change direction if needed
                    def nothing(tello: Tello):
                        common.executed = True
                        return 0    
                    run_pad = execute(nothing)
                case 2:
                    run_pad = execute(tunnel)
                case 3:
                    run_pad = execute(go_through)
                case 4:
                    run_pad = execute(rotate)
                case 5:
                    # run_pad = execute(up)
                    # idk, can add other functions here
                    pass
                case 6:
                    # run_pad = execute(down)
                    # idk, can add other functions here
                    pass
                case 7:
                    run_pad = execute(around)
                case 8:
                    if common.config['switch_mode']:
                        common.config['mode'] = 1
                        common.config['switch_mode'] -= 1
                        common.mode_switched = True
                        common.pads_permanent = [
                            1, 2, 4] if common.config['mode'] == 2 else list(range(1, 5))
                    else:
                        run_pad = execute(land)
    return run_pad
