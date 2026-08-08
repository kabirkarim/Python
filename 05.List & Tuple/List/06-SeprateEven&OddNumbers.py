# Separate Even and Odd Numbers
listOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumbers = []
oddNumbers = []

for number in listOfNumbers:
    if number % 2 == 0:
        evenNumbers.append(number)
    else:
        oddNumbers.append(number)

print("The even numbers in the list are:", evenNumbers)
print("The odd numbers in the list are:", oddNumbers)