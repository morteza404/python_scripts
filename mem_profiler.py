#!/usr/bin/env python3

from memory_profiler import profile

@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    aa = bytearray(1524288000)
    del b
    return a

if __name__ == "__main__":
    my_func()
