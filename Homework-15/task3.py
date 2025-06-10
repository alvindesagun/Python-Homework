# Create the country_capitals dictionary
capitals = {
    'USA': 'Washington, D.C.',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Japan': 'Tokyo',
    'UK': 'London'
}

# Prompt the user to enter a country name
print('-'*100)
print('FYI - My dictionary is limited to the following countries only - USA, France, Germany, Japan, UK')
print('-'*100)
print()
country = input('Enter a country name to find its capital: ')
print()
# Check if the entered country is in the dictionary
if country in capitals:
    capital = capitals[country]
    print(f'The capital of {country} is {capital}.')
    print()
else:
    print(f'Sorry, I don\'t have the capital for {country} in my dictionary.')
    print()
