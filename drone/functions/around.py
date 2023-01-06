import drone.common as common
from djitellopy import Tello


def around(tello: Tello):
    times = common.config['around']
    while times:
        if common.padId in range(1, 9):
            if common.change:
                print(f"go to mission pad {common.padId}")
                tello.go_xyz_speed_mid(
                    0, 0, common.config["init_height"], common.config["speed"], common.padId)
                common.change = False
        print(f"Going around.")
        tello.move_right(common.config['around_x'])
        tello.move_forward(common.config['around_y'])
        tello.move_left(common.config['around_x'])
        times -= 1
