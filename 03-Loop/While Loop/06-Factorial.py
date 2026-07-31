# Write a program to calculate the factorial of a number by the user using a while loop. The factorial of a number is the product of all positive integers from 1 to that number.
num=int(input("Enter a number: "))
factorial=1
count=1
while count<=num:
    factorial*=count
    count+=1
print(f"The factorial of {num} is {factorial}")
