#!/usr/bin/env python3

def fibo(n):
    a, b = 0, 1
    for _ in range(0, n):
        a, b = b, a + b
    return a

print(fibo(5))
