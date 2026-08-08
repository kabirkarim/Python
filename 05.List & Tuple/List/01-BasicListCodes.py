# Create a list of 5 numbers and print the 1st and last elements.
list_of_numbers = [10, 20, 30, 40, 50]
# print List
print("The list of numbers is:", list_of_numbers)

# Print the 1st and last elements
print("The first element is:", list_of_numbers[0])
print("The last element is:", list_of_numbers[-1])

#print the length of the list
print("The length of the list is:", len(list_of_numbers))

# Change the second element of a list to 100.
list_of_numbers[1] = 100
print("The updated list of numbers is:", list_of_numbers)

# Add an element to the end of a list using append().
list_of_numbers.append(60)
print("The list after appending 60 is:", list_of_numbers)

# Insert "Python" at index 2.
list_of_numbers.insert(2, "Python")
print("The list after inserting 'Python' at index 2 is:", list_of_numbers)

# Remove a particular element from a list.
list_of_numbers.remove(30)
print("The list after removing 30 is:", list_of_numbers)

# Delete the last element from a list.
list_of_numbers.pop()
print("The list after deleting the last element is:", list_of_numbers)

# Check whether 25 exists in a list.
if 25 in list_of_numbers:
    print("25 exists in the list.")
else:
    print("25 does not exist in the list.")