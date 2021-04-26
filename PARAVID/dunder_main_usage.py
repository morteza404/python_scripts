''' 
    forward declare a function
    how use function before definition?!
    by import project name & using:
                                    if __name__ == '__main__'

'''

import dunder_main_usage

print('information about this program :\n   {}'.format(__doc__))

# show_list()
if __name__ == "__main__":
    dunder_main_usage.show_list()

lst = []

def show_list():
    print('for exit type Z')
    while True:
        s = input('enter your list: ')
        if s == 'Z':
            break
        lst.append(s)
    print('your list is : \n {}'.format(lst))

    
