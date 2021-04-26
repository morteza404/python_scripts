# noun --> class, object 
# verb  --> method
# adjective --> attribute

'''
class Thief:
    # attribute --> adjective
    sneaky = True

    # method --> verb
    def sneak(self):
        print('that object sealed!')
'''
import random

class Character:
    def __init__(self, name, **kwargs):
        self.name = name
        for key,value in kwargs:
            setattr(self, key, value)

class Thief(Character):
    sneaky = True

    def __init__(self, name, sneaky = True, **kwargs):
        # super point to parent
        super().__init__(name, **kwargs)
        self.sneaky = sneaky
        for key,value in kwargs.items():
            setattr(self, key, value)

    def pick_pocket(self):
        # print('called by {}'.format(self))
        return bool(random.randint(0,1))
    
    def hide(self, light_level):
        return self.sneaky and light_level == 10

# DRY ==> Don't Repeat Yourself (by using inheritance)

    
        
        