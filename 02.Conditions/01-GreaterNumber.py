# Write a C program to check the first number is greater than the second number.
num1=int(input("Enter 1st Number: "))
num2=int(input("Enter 2nd Number: "))
if(num1>num2):
    print(f"{num1} is greater than {num2}")
elif(num1<num2):
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num2} is equall to {num1}")

