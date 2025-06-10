print('-'*100)
print('This program calculates the number days, weeks, and hours based on users input of years')
print('-'*100)
print()
years = int(input('Please enter the number of years you want to calculate: '))

days = 365*years
weeks = 52*years
hours = 24*365*years

print()
print(f'There are {days} days in {years} years')
print(f'There are {weeks} weeks in {years} years')
print(f'There are {hours} hours in {years} years')
print()

