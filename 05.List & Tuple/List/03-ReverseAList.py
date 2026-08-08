# Reverse a list.
list_of_numbers = [10, 20, 30, 40, 50]

# with Using Reverse
list_of_numbers.reverse()
print("The reversed list is:", list_of_numbers)

# Without Using Reverse: Method 1
reversed_list = list_of_numbers[::-1]
print("The reversed list is:", reversed_list)

# Without Using Reverse: Method 2
reversed_list = []
for i in range(len(list_of_numbers) - 1, -1, -1):
    reversed_list.append(list_of_numbers[i])
print("The reversed list is:", reversed_list)