# Find the second-largest number in a list.
list_of_numbers = [10, 20, 30, 40, 50]

# Method 1: Using sort() method
list_of_numbers.sort(reverse=True)
second_largest = list_of_numbers[1]
print("The second-largest number in the list is:", second_largest)

# Method 2: Without using sort() method
first_largest = list_of_numbers[0]
second_largest = float('-inf')
for number in list_of_numbers:
    if number > first_largest:
        second_largest = first_largest
        first_largest = number
    elif number > second_largest and number != first_largest:
        second_largest = number
print("The second-largest number in the list is:", second_largest)
