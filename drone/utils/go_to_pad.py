import drone.common as common


def go_to_pad(pad: int) -> None:
    print(f"go to mission pad {pad}")
    common.tello.go_xyz_speed_mid(
        0, 0, common.height, common.config["speed"], pad)
