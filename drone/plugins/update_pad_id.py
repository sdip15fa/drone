import drone.common as common


def on_change() -> None:
    common.executed = False
    common.change = True


def update_pad_id() -> None:
    if common.end:
        return
    new_pad_id = common.tello.get_mission_pad_id()
    print(f"detected pad id: {new_pad_id}")
    if new_pad_id in range(1, 9) and common.padId != new_pad_id:
        common.prev = common.padId
        common.padId = new_pad_id
        print("new pad id", common.padId)
        on_change()
