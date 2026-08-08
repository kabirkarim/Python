# Count how many even and odd numbers are in a list.
list_of_numbers = [10, 21, 32, 43, 54, 65, 76, 87, 98]
count_even = 0
count_odd = 0
for number in list_of_numbers:
    if number % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("The count of even numbers in the list is:", count_even)
print("The count of odd numbers in the list is:", count_odd)