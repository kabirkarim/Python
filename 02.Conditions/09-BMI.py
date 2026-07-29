# Write a C program that takes a person's height (in meters) and weight (in kilograms) as input and uses if-else
# statements to calculate and print their BMI (Body Mass Index) category based on the following categories:
# Underweight: BMI < 18.5
# Normal Weight: 18.5 <= BMI < 25
# Overweight: 25 <= BMI < 30
# Obese: BMI >= 30

height = float(input("Enter height (in meters): "))
weight = float(input("Enter weight (in kilograms): "))

# Calculate BMI
bmi = weight / (height ** 2)

print(f"\nBMI = {bmi:.2f}")

# Determine BMI Category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal Weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")