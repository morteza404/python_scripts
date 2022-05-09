"""
    this module show how tuple unpacking works.
"""

SNACKS = [('bacon', 350), ('donut', 240), ('muffin', 190)]

for rank, (name, calories) in enumerate(SNACKS, 1):
    print(f"#{rank}: {name} has {calories} calories.")
    