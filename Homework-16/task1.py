print()
print('-'*80)
print('Task 1')
print('Program calls a function called merge_lists that takes two lists as input \n\
and returns a new list that contains all the elements from both input lists in the same order')
print('-'*80)
print()

def merge_lists(list1, list2):
  merge_list = list1 + list2
  return merge_list

if __name__ == '__main__':
    def get_list(user_input):
        user_input = input(user_input)
    # Split the input string by commas and remove leading/trailing whitespace from each item
    # If the input is empty, return an empty list

        if user_input.strip() == '':
            return []
        return [item.strip() for item in user_input.split(',')]

    # Get the first list from the user
    list_1 = get_list('Enter your first list separated by commas (e.g. a,b,c,d,e,f): ')

    # Get the second list from the user
    list_2 = get_list('Enter your second list separated by commas (e.g. 1,2,3,4,5): ')

    # Merge the user-provided lists
    result = merge_lists(list_1, list_2)

    print(f'\nYour first list: {list_1}')
    print(f'Your second list: {list_2}')
    print(f'Your merged List: {result}')







