def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper

@do_twice
def say_hello():
    print("hello")

say_hello()