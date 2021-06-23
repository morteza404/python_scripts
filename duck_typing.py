#!/usr/bin/env python3

"""
    https://realpython.com/lessons/duck-typing/

    duck typing. 
    This term comes from the saying “If it walks like a duck, and it quacks like a duck, then it must be a duck.”
    Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines. 
    When you use duck typing, you do not check types at all. Instead, you check for the presence of a given method or attribute.

    For example, you can call len() on any Python object that defines a .__len__() method:

"""

class Hobbit():
    def __len__(self):
        return 1000


hobbit = Hobbit()

print(len(hobbit))

print(len("hobbit"))

try:
    print(len(10))
except TypeError:
    print("object of type 'int' has no len()")
