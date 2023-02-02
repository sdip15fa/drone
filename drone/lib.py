import time
import threading
from typing import Callable

StartTime = time.time()


class set_interval:
    def __init__(self, action: Callable, interval: int):
        self.interval = interval / 1000
        self.action = action
        self.stopEvent = threading.Event()
        thread = threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self):
        nextTime = time.time() + self.interval
        while not self.stopEvent.wait(nextTime - time.time()):
            nextTime += self.interval
            self.action()

    def cancel(self):
        self.stopEvent.set()
