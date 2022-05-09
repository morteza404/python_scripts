"""
    Often, you will want to iterate over a list and also know the index of
    the current item in the list.
    Python provides the enumerate built-in function to address this situation.
    enumerate wraps any iterator with a lazy generator.
    enumerate yields pairs of the loop index and the next value from the given iterator
"""

FLAVORS = ['vanilla', 'chocolate', 'pecan', 'strawberry']

for i, flavor in enumerate(FLAVORS, 1):
    print(f"{i}: {flavor}")
