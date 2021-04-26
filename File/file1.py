f = open('a.txt')
print(f.read())

'''
    file opening types:
    r : only for read , if file doesnt exist catch error.
    r+ : for read and write, if file doesnt exist catch error.
    w : only for write , if file doesnt exist doesnt catch error and makes it. previous text clean and text rewrite.
    w+ : for read and write, if file doesnt exist doesnt catch error and makes it
    a : write text in end of file. if file doesnt exist doesnt catch error and makes it
    a+ : same a, but get write access 
    
'''