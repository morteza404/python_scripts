import numba
from time import time
from dis import dis

def timeit(function):
    def wrapper(*args, **kwargs):
        start = time()
        function(*args, **kwargs)
        end = time()
        print(f"{function.__name__}, result: {function(*args, **kwargs)}, {end - start} seconds.")
    return wrapper

@timeit
def pure_sum():
    n = 0 
    for i in range(1, 1_000_000_001):
        n += i
    return n

@timeit
def builtin_sum():
    return sum(range(1, 1_000_000_001))

@timeit
@numba.jit
def jit_sum():
    n = 0 
    for i in range(1, 1_000_000_001):
        n += i
    return n

@timeit
@numba.jit
def jit_builtin_sum():
    return sum(range(1, 1_000_000_001))

# pure_sum()

# builtin_sum()

jit_sum()

# jit_builtin_sum()

# dis(pure_sum)

# dis(builtin_sum)

# dis(jit_sum)
