# Code 8: This program will interchange the values of two variables using arithmetic operations.
# Store input numbers
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
# Display original values
print("Before interchange: num1 =", num1, "and num2 =", num2)
# Interchange values using arithmetic operations
num1 = float(num1) + float(num2)
num2 = num1 - float(num2)
num1 = num1 - float(num2)
# Display interchanged values
print("After interchange: num1 =", num1, "and num2 =", num2)