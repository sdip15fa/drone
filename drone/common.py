from djitellopy_reduced import Tello

from drone.utils.get_config import get_config

config: dict[str, str] = get_config()

tello: Tello = Tello(host=config["ip"])

prev: int = 0
padId: int = -1
executed: bool = False
end: bool = False
change: bool = False

mode_switched: bool = False

pads_permanent: list = [1, 2, 4] if config['mode'] == 2 else list(range(1, 5))
