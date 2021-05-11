#!/usr/bin/env python3

from functools import partial

"""
Partial functions allow one to derive a function with x parameters to a 
function with fewer parameters and fixed values set for the more limited function.
"""

def multiply(x,y):
    return x * y

multiply2 = partial(multiply,2)

print(multiply2(4))