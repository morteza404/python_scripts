from time import time

def calc_time(func):
    def wrapper(*args):
        begin = time()
        func(*args)
        end = time()
        with open("time.txt", mode="a") as target:
            target.write(f"the {func.__name__} taken time is : {end-begin} seconds.\n")
        # print(f"the {func.__name__} taken time is : {end-begin} seconds.")
    return wrapper
