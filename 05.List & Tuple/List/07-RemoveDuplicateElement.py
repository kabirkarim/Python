# Remove Duplicate Elements
# Given the following list:
# numbers = [1, 2, 2, 3, 4, 3, 5, 1]
# Create a new list that contains each element only once.
# Expected Output:
# [1, 2, 3, 4, 5]

numbers = [1, 2, 2, 3, 4, 3, 5, 1]

# Method 1: Using set()
unique_numbers = list(set(numbers))
print("The list with unique elements is:", unique_numbers)

# Method 2: Without using set()
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print("The list with unique elements is:", unique_numbers)

# Method 3: Using dictionary keys
unique_numbers = list(dict.fromkeys(numbers))
print("The list with unique elements is:", unique_numbers)
