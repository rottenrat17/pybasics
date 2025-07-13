#stage 4
#less go
print('Welcome to command-line program')

my_lists = []
while True:
    print('\nChoose a number you want to do :')
    print('1.Reverse a word')
    print('2.Add items to a list')
    print('3.View the list')
    print('4.Remove items')
    print('5.Sort the list')
    print('6.Exit')

    choice = input('Enter your choice: ').strip()
    if choice == '1':
        reversed_word = input('Enter the word to reverse: ')
        print(f'Reversed: {reversed_word[::-1]}')

    elif choice == '2':
        item = input('Enter the list to add: ')
        my_lists.append(item)
    elif choice == '3':
        print(f"lists: {my_lists}")
    elif choice == '4':
        removed_list = input('Enter the list to remove: ')
        if removed_list in my_lists:
            my_lists.remove(removed_list)
            print(f'Removed: {removed_list}')
        else:
            print('List not found')
    elif choice == '5':
            my_lists.sort()
            print(f'Sorted: {my_lists}')
    elif choice == '6':
        print('Goodbye')
        break
    else:
        print('Invalid choice, Enter between 1 and 6.')
