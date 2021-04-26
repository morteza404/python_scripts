mylist = list(range(100))

result = [item for item in mylist if item%3 == 0 or item%5 == 0]

print(result)