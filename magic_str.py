class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name.title()}, age={self.age})"    

p = Person("pankaj", 34)

print(p)
