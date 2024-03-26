from timeit import default_timer as timer

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = timer()
        result = func(*args, **kwargs)
        end_time = timer()
        seconds = end_time - start_time

        if seconds < 60:
            print("INFO: {} took {} seconds to execute.".format(func.__name__, round(seconds, 2)))
        elif seconds < 3600:
            minutes, seconds = divmod(seconds, 60)
            print("INFO: {} took {} minutes {} seconds to execute.".format(func.__name__, int(minutes), int(seconds)))
        else:
            hours, remainder = divmod(seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            if minutes == 0:
                print("INFO: {} took {} hours {} seconds to execute.".format(func.__name__, int(hours), int(seconds)))
            else:
                print("INFO: {} took {} hours {} minutes {} seconds to execute.".format(func.__name__, int(hours), int(minutes), int(seconds)))

        return result

    return wrapper