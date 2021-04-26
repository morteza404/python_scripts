from time import time

def calc_time(func):
    def wrapper(*args):
        begin = time()
        func(*args)
        end = time()
        print(f"the function {func.__name__} execution taken {end - begin} seconds.")
    return wrapper