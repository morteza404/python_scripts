try:
    count = int(input('give me a number : '))
except ValueError:
    print('that is not a number!')

print(count + 1)