print()
print('-'*100)
print('Task 2 - Lists, Tuples and Dictionary')
print('-'*100)
print()
# Create tuples 'food' and 'calories'
food_tuple = ('Apple', 'Banana', 'Orange', 'Mango', 'Strawberry', 'Grape', 'Mandarin', 'Strawberry')
calories_tuple = (52, 96, 62, 605, 33, 68, 50, 33)

# Convert tuples to lists
foods_list = list(food_tuple)
calories_list = list(calories_tuple)

# Print the 5th element (Strawberry) and its caloric value
print(f"The 5th element is: {foods_list[4]} - ({calories_list[4]} kcal)")

# Print the second last food and its caloric value
print(f"The second last food is: {foods_list[-2]} - ({calories_list[-2]} kcal)")

# Print all unique foods in the list
unique_foods = sorted(list(set(foods_list)))
print("Unique foods:", unique_foods)

# Create a dictionary with unique food keys and their caloric values
food_calorie_dict = {}
for i in range(len(food_tuple)):
    food_calorie_dict[food_tuple[i]] = calories_tuple[i]

print("Food-calorie dictionary:", food_calorie_dict)
print()
