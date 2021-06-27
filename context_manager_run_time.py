from contextlib import contextmanager
from time import time

@contextmanager
def run_time(discription):
    start = time()
    try:
        yield
    finally:
        end = time()
        print(f"the {discription} function took {end - start} seconds to run.")

def mul(a, b):
    return pow(2,a) * b

with run_time("mul"):
    mul(20, 150)
