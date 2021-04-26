import random

from characters import Character
from attributes import Agile, Sneaky

class Thief(Agile, Sneaky, Character):
    def pick_pocket(self):
        return self.sneaky and bool(random.randint(0,1))


# issubclass(Thief, Character) : True