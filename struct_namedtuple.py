#!/usr/bin/env python3

from collections import namedtuple
from math import sqrt

"""
	create c struct like in python by using namedtuple.
	They can be used similarly to struct or other common record types, except that they are immutable.
	you should use named tuples instead of tuples anywhere you think object notation will make your code 
	more pythonic and more easily readable.  
"""

Employee = namedtuple("Employee", ["name", "age", "salary"])

emp = Employee("ali", "30", "1000")

print(emp)
print(emp.name)
print(emp.age)
print(emp.salary)

print(id(emp))

Point = namedtuple("Point", ["x", "y"])
pt1 = Point(2,3)
pt2 = Point(4,5)

line_length = sqrt((pt1.x-pt2.x)**2 + (pt1.y-pt2.y)**2)

print(line_length)