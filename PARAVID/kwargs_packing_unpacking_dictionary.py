def packer(**kwargs):
    print(kwargs)

packer(name = 'ali', num = 42)

def packer2(name = None, **kwargs):
    print(kwargs)

packer2(name = 'ali', num = 42)

def unpacker(name = None, family = None):
    if name and family:
        print('Hi {} {}'.format(name, family))
    else:
        print('Hi no name')

unpacker(**{'family':'naghavi', 'name':'hasan'})