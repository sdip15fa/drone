import threading

def set_interval(func, ms):
    def func_wrapper():
        set_interval(func, ms)
        func()
    t = threading.Timer(ms / 1000, func_wrapper)
    t.start()
    return t
