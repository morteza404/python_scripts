from decorators import add_word, do_twice, mul_10, pow_even_two, multiply, calculate_time


@do_twice
def say_hello():
    print("hello")

# say_hello()

@pow_even_two
def pow_two(num):
    return num * num

# print(pow_two(100))

# @calculate_time
@multiply
def add(*args):
    return sum(args)

# print(add(1,2,3))

# print(add(4,5,6))

# print(add(1,1,2))

@add_word("bye")
def say_bye():
    return "good "


# print(say_bye())

@mul_10(10)
def add_2(num1, num2):
    return num1 + num2

print(add_2(2,3))

@calculate_time
def mul_1024():
    print(pow(2,25) * 1024)