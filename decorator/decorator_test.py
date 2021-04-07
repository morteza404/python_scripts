"""
    we have pow_two() function that return num ^ 2.
    we need pow_two() return num ^ 2 if num be even.
    we can do this by checking in body of function.
    without changing function body, we can do this by using decorator! 

"""



def pow_even_two(function):
    def check_even(num):
        return function(num) if (num % 2 == 0) else num
    return check_even


@pow_even_two
def pow_two(num):
    return num * num

print(pow_two(100))


# without using @decorator

"""

num = pow_even_two(pow_two)

print(num(5))
 
""" 