def multiply(function):
    def wrapper(*args):
        return function(*args) *2
    return wrapper


@multiply
def add(*args):
    return sum(args)

print(add(1,2,3))

print(add(4,5,6))

print(add(1,1,2))
