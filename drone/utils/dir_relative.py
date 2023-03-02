def dir_oppo(dir: int):
    """
    The dir_oppo function takes a direction and returns the opposite direction.
    For example, dir_oppo(2) returns 4.

    :param dir: int: Determine the direction of the next move
    :return: The opposite direction of the input
    :doc-author: Trelent
    """
    if dir + 2 > 4:
        return dir - 2
    else:
        return dir + 2


def dir_left(dir: int):
    """
    The dir_left function takes a direction and returns the left direction.
    For example, dir_left(2) would return 4.
    
    :param dir: int: Specify the direction of the robot
    :return: The direction to the left of the given direction
    :doc-author: Trelent
    """
    match dir:
        case 1:
            return 3
        case 2:
            return 4
        case 3:
            return 2
        case 4:
            return 1


def dir_right(dir: int):
    """
    The dir_right function takes a direction and returns the right direction.
    
    :param dir: int: Specify the direction that we want to turn
    :return: The direction to the right of the given direction
    :doc-author: Trelent
    """
    match dir:
        case 1:
            return 4
        case 2:
            return 3
        case 3:
            return 1
        case 4:
            return 2

def dir_back(dir: int):
    """
    The dir_back function takes a direction and returns the opposite direction.
    For example, dir_back(2) returns 1.
    
    :param dir: int: Determine which direction the robot is currently facing
    :return: The opposite direction
    :doc-author: Trelent
    """
    match dir:
        case 1:
            return 2
        case 2:
            return 1
        case 3:
            return 4
        case 4:
            return 3
