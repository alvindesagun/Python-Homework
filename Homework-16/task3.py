print()
print('-'*80)
print('Task 3')
print('This is  Python program that takes a user\'s name as input and prints a greeting message. \n\
If the name is \'Alice\' or \'Bob\', the program will print \'Hello, Alice/Bob!\' Otherwise, \n\
it should print \'Hello, guest!\'')
print('-'*80)
print()

# create a user list
user_list=['Alice', 'Bob']

# Ask for input
username=input('Pleaes enter your username: ')

if username in user_list:
    print(f'Hello',username) 
    print()
else:
    print(f'Hello guest')
    print()
