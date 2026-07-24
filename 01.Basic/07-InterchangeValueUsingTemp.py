#Code 7: This program will interchange the values of two variables using a temporary variable.
# Store input numbers
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
# Display original values
print("Before interchange: num1 =", num1, "and num2 =", num2)
# Interchange values using a temporary variable
temp = num1
num1 = num2
num2 = temp
# Display interchanged values
print("After interchange: num1 =", num1, "and num2 =", num2)
