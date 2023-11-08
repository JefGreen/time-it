import time


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def log_duration(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        duration = "{:.2f}".format((time.time() - start_time))
        formated_kwargs = ', '.join([f'{key}: {bcolors.OKBLUE}{value}{bcolors.ENDC}' for key, value in kwargs.items()])

        print(f'{duration}s for {bcolors.BOLD}{func.__name__}{bcolors.ENDC} {formated_kwargs}')
        return result
    return inner
