from time import sleep
import drone.common as common
from threading import Timer
from drone.plugins.monitor import monitor
from drone.plugins.update_pad_id import update_pad_id
from drone.utils.do_operation import do_operation
from drone.utils.init_drone import init_drone
from drone.lib import set_interval


def main() -> None:
    monitor_interval: Timer = set_interval(monitor, 2000)
    update_pad_interval: Timer = set_interval(update_pad_id, 200)

    init_drone()

    while True:
        if common.end:
            update_pad_interval.cancel()
            monitor_interval.cancel()
            return
        # elif KeyboardInterrupt:
        #    common.tello.land()
        else:
            try:
                do_operation(common.padId)
            except Exception as e:
                print(e)
