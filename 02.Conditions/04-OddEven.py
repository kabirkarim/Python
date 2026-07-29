# A number is taken input from the user; Write a program to determine if it is an odd number or an even number.
number=int(input("Enter The Number: "))
if number%2==0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")