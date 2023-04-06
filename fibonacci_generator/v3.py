import itertools

def fibonnacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a+b

gen = fibonnacci()

slice = itertools.islice(gen, 15)

print(list(slice))
