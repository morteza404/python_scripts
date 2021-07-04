
"""
split() Parameters
split() method takes a maximum of 2 parameters:

separator (optional)- It is a delimiter. The string splits at the specified separator.
If the separator is not specified, any whitespace (space, newline etc.) string is a separator.
maxsplit (optional) - The maxsplit defines the maximum number of splits.
The default value of maxsplit is -1, meaning, no limit on the number of splits.
"""

grocery = 'Milk, Chicken, Bread, Butter'

# maxsplit: 2
print(grocery.split(', ', 2))

# maxsplit: 1
print(grocery.split(', ', 1))

# maxsplit: 5
print(grocery.split(', ', 5))

# maxsplit: 0
print(grocery.split(', ', 0))