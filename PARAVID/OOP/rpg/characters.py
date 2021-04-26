import random

class Character:
    # magic methos : methodes with __<name>__
    def __init__(self, name = '', **kwargs):
        if not name:
            raise ValueError('name is required.')
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{} : {}'.format(self.__class__.__name__, self.name)

# sepehr.__class__.__name__ : return obj class name
