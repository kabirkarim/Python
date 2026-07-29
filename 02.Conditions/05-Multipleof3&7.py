# Write a program that a number input from user . Check whether the number is multiple of 3 or 7 or both. (using || operator).
number = int(input("Enter a number: "))
if (number%3==0 and number%7==0):
    print(f"{number} is a multiple of 3 and 7 both.")
elif(number%3==0):
    print(f"{number} is a multiple of 3.")
elif(number%7==0):
    print(f"{number} is a multiple of 7")
else:
    print("Not a multiple of 3 and 7.")