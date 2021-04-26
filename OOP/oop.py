'''
    this program is about class variable
    Morteza
    2017/10/14

'''
class Person:
    #class name is PascalCase
    count = 0
    #class var name is camelCase
    def __init__(self):
       # to get class variable, whether in class or out of class, we use ClassName.varname
       Person.count += 1
       #print('total number of objs is : {} .' .format(Person.count))

    def func(self):
        #method name is camelCase
        print('total number of obj is : {}' .format(Person.count))

obj = Person()
obj.func()
obj2 = Person()
obj2.func()
print(__doc__)