name = input('please enter your name: ')
age = int(input('how old are you ,{0} ? '.format(name)))
if 18 <=age < 31:
    print('welcome to club 18-30 {0} '.format(name))
else:
    print("i'm sorry! you are very young :)")
