import pdb

my_list = [5, 2, 1, True, 'abcdefg', False, 4]

pdb.set_trace()

# import pdb; pdb.set_trace()

del my_list[3]
del my_list[4]
del my_list[3]
print(my_list)

