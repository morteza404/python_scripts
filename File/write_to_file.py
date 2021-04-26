f = open('C:\\Users\\Nikan\\Desktop\\test.txt', 'w')

for i in range(1,11):
    f.write(str(i))
    f.write(',')
    f.write(str(i**2))
    f.write('\n')
f.close()