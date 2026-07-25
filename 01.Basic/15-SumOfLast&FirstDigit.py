# Code 15: Sum of first and last digit of a 4-digit number
number = int(input("Enter a 4-digit number: "))

first_digit = number // 1000
last_digit = number % 10

sum_of_digits = first_digit + last_digit

print(f"First digit: {first_digit}")
print(f"Last digit: {last_digit}")
print(f"Sum of first and last digit: {sum_of_digits}")