# TODO call one function (with one parameters) with multiple values

f = lambda x : x ** 3 - 4

lst = [10, 15, 20, 25, 30, 35, 40, 45, 50]

f_lst = list(map(f,lst))

print(f_lst)

# TODO call one function (with multiple parameters) with multiple values

f = lambda x , y : x ** y - 4

lst1 = [ 10, 15 , 20 , 25, 30, 35, 40, 45, 50]

lst2 = [3,2, 2.3, 2.5, 3.1, 2.7, 4.1, 2.8, 1.8]

f_lst = list(map(f,lst1, lst2))

print(f_lst)
