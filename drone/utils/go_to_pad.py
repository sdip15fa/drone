import drone.common as common


def go_to_pad(pad: int) -> int:
    if pad in range(1, 9):
        if common.change:
            print(f"go to mission pad {pad}")
            common.tello.go_xyz_speed_mid(
                0, 0, common.config["init_height"], common.config["speed"], pad)
            common.change = False
            return pad
        else:
            return 1
