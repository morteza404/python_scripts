#!/usr/bin/env python3

import os

base_dir = "/home/shahbazi/Desktop"

path = os.path.join(base_dir, "results", "put_o1_curl.png")

size = os.path.getsize(path)

name = os.path.basename(path)

print(f"size of {name} is {size} bytes.")
