from djitellopy import Tello

from drone.utils.get_config import get_config

config = get_config()

tello: Tello = Tello(host=config["ip"])

test = False

prev: int = 0
padId: int = -1
executed: bool = False
end: bool = False
change: bool = False
