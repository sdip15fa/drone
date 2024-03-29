from time import sleep
import drone.common as common


def init_drone() -> None:
    # wait until connection is established
    common.tello.connect(True)
    print("Tello connected")

    common.connected = True

    sdk = common.tello.query_sdk_version()
    print(f"SDK version: {sdk}")
    battery = common.tello.get_battery()
    print(f"battery: {battery}%")

    print("enabling mission pads detection")
    common.tello.enable_mission_pads()

    common.padId = common.tello.get_mission_pad_id()
    print(f"mission pad id: {common.padId}")

    print("Taking off")
    common.tello.takeoff()
    print("Took off")

    while True:
        try:
            if common.tello.query_distance_tof() >= 10:
                break
        except:
            pass
        # sleep(1)

    common.tello.set_speed(common.config["speed"])

    if not common.tello.is_flying:
        print("Tello not flying")
        return

    height = common.tello.get_height()

    if height + 20 < common.height:
        print(f"Moving up to {common.height}cm")
        common.tello.move_up(common.height - height)
    elif height - 20 > common.height:
        print(f"Moving down to {common.height}cm")
        common.tello.move_down(height - common.height)

    common.initialized = True
    print("Tello initialized")
