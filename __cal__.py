#!/usr/bin/env python3

"""
    https://www.geeksforgeeks.org/__call__-in-python/
    The __call__ method enables Python programmers to write classes where 
    the instances behave like functions and can be called like a function. 
    When the instance is called as a function; 
    if this method is defined, x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...).
"""

class Test:
    def __init__(self):
        print("Instance Created")

    def __call__(self):
        print("Instance is called via special method")

obj = Test()
obj()

class Test2:
    def __init__(self):
        print("Instance Created")

    def __call__(self, a, b):
        print(a ** b)

obj2 = Test2()
obj2(3, 4)

class HttpTracer:
    def __init__(self):
        print("Instance Created")

    def __call__(self, method, status_code):
        print(f"method type is : {method} and status code is : {status_code}.")

obj3 = HttpTracer()
obj3("HEAD", "204")