# code refactoring

# have a HELP command
def show_help():
    # print out instructions on how use app
    print('what should we pick up at the store?')
    print("""
            enter 'DONE' to stop adding items.
            enter 'SHOW' to stop adding items.
            enter 'HELP' to stop adding items.
          """)

# have a SHOW command
def show_list():
    print('here is your list: ')
    for item in shopping_list:
    # print out the list
        print(item)

def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print('Added {}. list now has {} items.'.format(new_item, len(shopping_list)))


   

# make a list to hold onto our items
shopping_list = []

show_help()


while True:
    # ask for new items
    new_item = input('> ')

    # be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue

    add_to_list(new_item)

show_list()

   

   




