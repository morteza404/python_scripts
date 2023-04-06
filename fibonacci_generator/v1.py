def fibonnacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a+b

gen = fibonnacci()

print(gen)
