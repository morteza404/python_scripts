"""
    zip keeps yielding tuples until any one of the wrapped iter-
    ators is exhausted. Its output is as long as its shortest input. This
    approach works fine when you know that the iterators are of the
    same length, which is often the case for derived lists creeated by list comprehensions.
    If you don’t expect the lengths of the lists passed to zip to
    be equal, consider using the zip_longest function from the itertools
    built-in module instead.
"""

from itertools import zip_longest


NAMES = ['Cecilia', 'Lise', 'Marie']

COUNTS = [10, 20]

print("--- using zip ---\n")

for name, count in zip(NAMES, COUNTS):
    print(name, count)

print("\n--- using zip_longest ---\n")

for name, count in zip_longest(NAMES, COUNTS):
    print(name, count)
