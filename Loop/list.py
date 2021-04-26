__author__ = 'Morteza'

ip = input('please enter ip address : ')
print(ip.count('.'))

name = input('please enter name : ')
print(name.count('e'))

names = ['Morteza','Saeed','Sajjad','MohammadReza']
names.append('Hamed')

for i in names:
    print('name is {} '.format(i))

even = [2,4,6,8]
odd = [1,3,5,7,9]
number = even + odd
print('numbers before sorting are: {}  '.format(number))
number.sort()
print('number after sorting are: {}  '.format(number))