from datetime import datetime

"""
    https://www.geeksforgeeks.org/str-vs-repr-in-python/

    str() is used for creating output for end user while repr() is mainly used for debugging and development. 
    repr’s goal is to be unambiguous and str’s is to be readable.
"""

date = datetime.now()

print(str(date))
print(date.__str__())

print(repr(date))
print(date.__repr__())