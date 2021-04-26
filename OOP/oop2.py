'''
    this program is about insrance variable and obj attrib
    Morteza
    2017/10/14
'''

class Person:
    #class var
    count = 0
    def __init__(self, name):
        #instance var, define: self.varname
        self.name = name
        print('{} created :)' .format(self.name))

obj = Person('Morteza')
#define more attrib for obj
obj.phone = '09821'
#delete attrib
#del obj.phone
print(obj.name)
print(obj.phone)
obj2 = Person('Reza')
print(obj2.name)
print(dir(obj))
print(dir(obj2))