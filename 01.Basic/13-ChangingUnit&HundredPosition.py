# Code 13: Reverse unit digit with hundred digit in a 5-digit number
number = int(input("Enter a 5-digit number: "))

unit_digit = number % 10
hundred_digit = (number // 100) % 10

print(f"Unit digit: {unit_digit}")
print(f"Hundred digit: {hundred_digit}")

number= number - unit_digit - hundred_digit * 100 + unit_digit * 100 + hundred_digit

print(f"Number after swapping unit and hundred digits: {number}")