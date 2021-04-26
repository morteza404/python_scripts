'''
    this program is about destructor
    Mortezaq
    2017/10/14
'''
class Person:
    def __init__(self, name):
        self.name = name
        print('{} created.' .format(name))

    def __del__(self):
        print('{} destroied.' .format(self.name))

obj = Person('Morteza')
del obj