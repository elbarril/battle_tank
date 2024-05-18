import time


def log_time_elapsed(event):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = event(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print("Event: %s" % event.__name__, "%.4f" % elapsed_time, "seconds")
        return result
    return wrapper
