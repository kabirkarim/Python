# Find the largest number in a list.

list_of_numbers = [10, 20, 30, 40, 50]

# With Using Max
max_number = max(list_of_numbers)
print("The largest number in the list is:", max_number)

# Without Using Max
max_number = list_of_numbers[0]
for number in list_of_numbers:
    if number > max_number:
        max_number = number
print("The largest number in the list is:", max_number)