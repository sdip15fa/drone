from djitellopy import Tello


def goToPad(tello: Tello) -> None:
    """autocorrect location to get as close to the mission pad as possible

    x and y directions only
    """
    # x direction
    x = tello.get_mission_pad_distance_x()
    while abs(x) >= 20:
        x = tello.get_mission_pad_distance_x()
        if x >= 20:
            if x > 500:
                tello.move_right(500)
            else:
                tello.move_right(x)
        elif x <= -20:
            if x >= -500:
                tello.move_left(abs(x))
            else:
                tello.move_left(500)
    # y direction
    y = tello.get_mission_pad_distance_y()
    while abs(x) >= 20:
        y = tello.get_mission_pad_distance_y()
        if y >= 20:
            if y > 500:
                tello.move_forward(500)
            else:
                tello.move_forward(x)
        elif x <= -20:
            if x >= -500:
                tello.move_back(abs(x))
            else:
                tello.move_back(500)
