from djitellopy_reduced import Tello
import drone.common as common

runs: int = 0
curve_runs: int = 0


def curve(tello: Tello):
    global runs, curve_runs

    speed = common.config["speed"] / 100 * 60
    if speed < 10:
        speed = 10
    
    times = (common.config["curve_times"][runs] if len(common.config["curve_times"]) > runs else 1) or 1

    for _ in range(times):
        x = common.config["curve_x"][curve_runs] if curve_runs < len(common.config["curve_x"]) else common.config["curve_x_default"]
        y = common.config["curve_y"][curve_runs] if curve_runs < len(common.config["curve_y"]) else common.config["curve_y_default"]
        z = common.config["curve_z"][curve_runs] if curve_runs < len(common.config["curve_z"]) else common.config["curve_z_default"]
        tello.curve_xyz_speed_mid(y / 2, x, z, y, 0, z, speed, common.running)
        curve_runs += 1

    common.executed = True
    runs += 1
