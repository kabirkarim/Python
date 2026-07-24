# Code 9: This program will find the sum of digits of an integer.
# In this program, we use // operator to perform integer division to extract each digit of the 5-digit integer. We then calculate the sum of these digits and display the result.
num = input("Enter an 5 digit integer: ")
num = int(num)
digit1 = num // 10000
digit2 = (num // 1000) % 10
digit3 = (num // 100) % 10
digit4 = (num // 10) % 10
digit5 = num % 10
sum_of_digits = digit1 + digit2 + digit3 + digit4 + digit5
print("The sum of digits of", num, "is:", sum_of_digits)
