### Change Behavior
class Calculate:
    def __init__(self, a):
        self.a = a
    def sum(self):
        print(self.a + 10)

def sum_20(self):
    print(self.a+20)

obj = Calculate(10)
obj.sum()
Calculate.sum = sum_20
obj.sum()

### Change Behavior
class B:
    def say_hello(self):
        print("hello")

def say_salam(self):
    print("salam")

B.say_hello = say_salam
obj = B()
obj.say_hello()

### Add Behavior
class A:
    def say_hello(self):
        print("hello")

def say_salam(self):
    print("salam")

A.say_salam = say_salam
obj = A()
obj.say_salam()
