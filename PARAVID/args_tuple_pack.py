def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(5,5))
print(add(32))
print(add(10,11,12))
print(add(5,5,15,14,20))


def add2(base, *args):
    total = base
    for num in args:
        total += num
    return total

print(add2(5,15))