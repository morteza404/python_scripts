#!/usr/bin/env python3

from decorators import calc_time
import mmap

@calc_time
def regular_io(filename):
    with open(filename, mode="r") as target:
        data = target.read()
        print(data)

@calc_time
def mmap_io(filename):
    with open(filename, mode="r") as target:
        with mmap.mmap(fileno=target.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            data = mmap_obj.read()
            print(data)
            # we can use mmap object as string and slice it !
            print(data[10:20])


if __name__ == "__main__":
    regular_io("data.txt")
    mmap_io("data.txt")