def primes(n):

    for c in range(2,n):
        if n % c == 0:
            return None
            break
    else:
        print(n)


for i in range(2,51):
    primes(i)