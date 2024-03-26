from timeit import default_timer as timer

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = timer()
        result = func(*args, **kwargs)
        end_time = timer()
        elapsed_time = end_time - start_time
        print("INFO: {} took {} seconds to execute.".format(func.__name__, round(elapsed_time, 2)))
        return result

    return wrapper