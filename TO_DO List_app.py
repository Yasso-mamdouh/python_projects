
user_input = 'random'
data = []


def show_menu():
    print('\nMenu:')
    print('1. Add an Item')
    print('2. Mark as read')
    print('3. View to-do Items')
    print('4. Exit')


print("\nWelcome in my simpple program:")

while user_input != '4':
    show_menu()
    user_input = input('Enter your choice: ')
    if user_input == '1':
        print('Add a new Item')
        new_item = input('What is to be done? ')
        data.append(new_item)
        print('Added item: ', new_item)
    elif user_input == '2':
        item = input('what it is to be marked as done? ')
        if item in data:
            data.remove(item)
            print('Removed item: ', item)
        else:
            print('Item not found')
    elif user_input == '3':
        print('View the to do items')
        item_counter = 1
        for item in data:
            print(f'Item-{item_counter}:{item}')
            item_counter +=1

    elif user_input == '4':
        print('Goodbye')
    else:
        print('Please enter one of 1, 2, 3 or 4')
