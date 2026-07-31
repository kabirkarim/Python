# Write a program that takes a number as input and uses a while loop to reverse and print the digits of that number. For example, if the input is 12345, the program should print 54321.

num=int(input("Enter a number: "))
reverse=0
remainder=None
while num>=1:
    remainder=num%10
    reverse=(reverse*10)+remainder
    num//=10

print(f"The reverse number is {reverse}")