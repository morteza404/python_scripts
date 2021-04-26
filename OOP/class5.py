class Person:
    #class variable
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1
        print("{} created.".format(name))

obj1 = Person('Morteza')
print(obj1.count)
obj2 = Person('Ali')
print(obj2.count)
obj3 = Person('Hassan')
print(obj3.count)