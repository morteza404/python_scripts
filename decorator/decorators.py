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