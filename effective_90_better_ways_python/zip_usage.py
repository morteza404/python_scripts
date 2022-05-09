"""
    zip wraps two or more iterators with a lazy generator.
    These tuples can be unpacked directly within a for statement.
"""

NAMES = ['Cecilia', 'Lise', 'Marie']

COUNTS = [len(a) for a in NAMES]

MAX_COUNT = 0

LONGEST_NAME = None

for name, count in zip(NAMES, COUNTS):
    if count > MAX_COUNT:
        LONGEST_NAME = name
        MAX_COUNT = count

print(LONGEST_NAME)
