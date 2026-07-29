# Write a program that shows whether the driver is insured or not. The conditions that are true are as follows:
# The driver is married.
# The driver is unmarried, male and is above the age of 30.
# The driver is unmarried, female and is above the age of 25.

gender = input("Enter your gender (Male/Female): ").upper()
age = int(input("Enter your age: "))
marital_status = input("Are you married? (Yes/No): ").upper()

if marital_status == "YES":
    print("Driver is insured.")
elif gender == "MALE" and age > 30:
    print("Driver is insured.")
elif gender == "FEMALE" and age > 25:
    print("Driver is insured.")
else:
    print("Driver is not insured.")
