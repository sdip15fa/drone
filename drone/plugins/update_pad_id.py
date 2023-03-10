from time import sleep
import drone.common as common

pads: int = 0


def on_change() -> None:
    global pads
    common.executed = False
    common.direction = (common.config['direction'][pads] if pads < len(
        common.config['direction']) else common.direction) or common.config["direction_default"]
    common.height = (common.config['height'][pads] if pads < len(
        common.config['height']) else common.height) or common.config["height_default"]
    print("direction", common.direction)
    pads += 1


def update_pad_id() -> None:
    if common.end:
        return
    new_pad_id = common.tello.get_mission_pad_id()
    print(f"detected pad id: {new_pad_id}")
    if new_pad_id in range(1, 9) and common.padId != new_pad_id and not (common.padId == new_pad_id and new_pad_id in common.config['blacklist_repeat_pads']):
        # if new_pad_id in range(1, 9) and common.detected == -1:
        #    sleep(1)
        common.detected = new_pad_id
        common.prev = common.padId
        common.padId = new_pad_id
        print("new pad id", common.padId)
        common.change = True
    else:
        common.detected = new_pad_id
