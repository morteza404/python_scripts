for i in range(1,11):
    print('num is {} and num power 2 is {} '.format(i,i**2))

number = "12,15,17,89,63,54,47"
for i in range(0,len(number)):
    if number[i] in '0123456789':
        print(number[i])