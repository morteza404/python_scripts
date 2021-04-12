from time import time

def do_twice(function):
    def wrapper():
        function()
        function()
    
    return wrapper

def multiply(function):
    def wrapper(*args):
        return function(*args) *2
    return wrapper

def pow_even_two(function):
    def check_even(num):
        return function(num) if (num % 2 == 0) else num
    return check_even

def calculate_time(function):
    def wrapper(*args, **kwargs):
        start = time()
        function(*args, **kwargs)
        end = time()
        print(f"{function.__name__} taken {end - start} seconds.")
    return wrapper


# decorator with arguments
def add_word(word):
    def middle(function):
        def wrapper(*args):
            return function(*args) + word
        return wrapper
    return middle

# decorator with arguments
def mul_10(num):
    def middle(function):
        def wrapper(*args):
            return function(*args) * num
        return wrapper
    return middle