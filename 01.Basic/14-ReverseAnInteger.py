# Code 14: Reverse a 4-digit number
number = int(input("Enter a 4-digit number: "))


thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
units_digit = number % 10

# Form the reversed number
reversed_number = units_digit * 1000 + tens_digit * 100 + hundreds_digit * 10 + thousands_digit

print(f"Reversed number: {reversed_number}")