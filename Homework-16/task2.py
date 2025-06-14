print()
print('-'*80)
print('Task 2')
print('This Python program asks the user to enter a number \n\
and prints whether it is positive, negative, or zero.')
print('-'*80)
print()

try:

    number = int(input('Please enter a number: '))

except ValueError:
    print('Please enter a valid integer')
    print()
else:
    if number > 0:
        print(f'You have entered a positive number')
        print()
    elif number < 0:
        print(f'You have entered a negative number')
        print()
    else:
        print(f'You have entered 0')
        print()

