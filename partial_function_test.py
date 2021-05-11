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

def f(a, b, c, x):
    return 1000*a + 100*b + 10*c + x
  
# A partial function that calls f with
# a as 3, b as 1 and c as 4.
g = partial(f, 3, 1, 4)
  
# Calling g()
print(g(5))

def add(a, b, c):
    return 100 * a + 10 * b + c
  
# A partial function with b = 1 and c = 2
add_part = partial(add, c = 2, b = 1)
  
# Calling partial function
print(add_part(3))