'''
    author : Morteza

    about : zip,lambda,map,inline if

'''

# ---------- zip function -------------

lst = range(100,201,10)

lst2 = range(1000,1201,10)

for i,j in zip(lst,lst2):
    print(i,j,i+j)

# ------------- map, lambda function, inline if ----------------

lst = [100,250,21,458,10,953,7,26,101]

print(list(map(lambda x:'Big' if x>100 else 'Small',lst))) 

print(__doc__)