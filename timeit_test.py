#!/usr/bin/env python3

import timeit

import_module = "import random"

testcode = """
def test(): 
    return random.randint(10, 100)
"""

print(timeit.repeat(stmt=testcode, setup=import_module, repeat=5))