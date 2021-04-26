'''
    this program is about destructor
    Morteza
    2017/10/14
'''
class Person:
    a = 1
    b = a
    #destructor
    def __del__(self):
        pass
'''
for func about attrib are:
    getattr()
    setattr()
    hasattr()
    delattr()
'''

obj = Person()
print(dir(obj))
print(id(Person.a))
print(id(Person.b))
del Person.a
#print(id(Person.a))  error : a there isn't