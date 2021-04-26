lst = []

for i in range(100):
    if i % 2 == 0:
        lst.append(i)

print(lst) 


lst = [i for i in range(50) if i % 2 == 0]   

print(lst)    