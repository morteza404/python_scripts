'''
    this program is about inheritance. python  has multi inheritance.
    Morteza
    14/10/2017
'''

class Person:
    def __init__(self, name):
        self.name = name
        print('{} created.' .format(self.name))

    def __del__(self):
         print('{} destroied.' .format(self.name))

obj = Person('Ali')
del obj

#ItMan inherits from Person
class ItMan(Person):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        print('{} with email {} created.' .format(self.name, self.email))
obj2 = ItMan('Saeed', 'saeed@email.com')
