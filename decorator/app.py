from decorators import do_twice, pow_even_two, multiply


@do_twice
def say_hello():
    print("hello")

say_hello()

@pow_even_two
def pow_two(num):
    return num * num

print(pow_two(100))

@multiply
def add(*args):
    return sum(args)

print(add(1,2,3))

print(add(4,5,6))

print(add(1,1,2))
