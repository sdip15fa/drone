import drone.common as common


def monitor() -> dict[str, int]:
    curr_height = common.tello.get_height()
    print(f"height: {curr_height} cm")
    battery_level = common.tello.get_battery()
    print(f"battery: {battery_level}%")
    temp = common.tello.get_temperature()
    print(f"temperature: {temp} °C")
    tof = common.tello.get_distance_tof()
    print(f"tof distance: {tof} cm")
    # speed = common.tello.query_speed()
    # print(f"speed: {speed}")
    print(f"mission pad id: {common.padId}")
    return {"height": curr_height, "battery": battery_level, "temperature": temp, "tof": tof}
