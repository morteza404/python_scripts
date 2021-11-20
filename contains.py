"""
    __ contains __ method is used to overload the “in” operator in python. 
    For example, you have a custom class MyClass 
    and you want to check if one instance is in another by using it.
"""

class MyClass():
    def __init__(self, name):
        self.name = name

    def __contains__(self, substr):
        if substr in self.name:
            return True
        return False

obj = MyClass("sadegh")
print("sad" in obj)
print("Sad" in obj)
