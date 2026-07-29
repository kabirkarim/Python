# Create a program that asks the user for their test score and the number of attendance days. Use nested if-else
# statements to determine their grade based on the following criteria:
# A: Score >= 90 and Attendance >= 90%
# B: Score >= 80 and Attendance >= 80%
# C: Score >= 70 and Attendance >= 70%
# D: Score >= 60 and Attendance >= 60%
# F: Otherwise

score = int(input("Enter your test score: "))
attendance = int(input("Enter your attendance percentage: "))

if score >= 90:
    if attendance >= 90:
        print("Grade: A")
    else:
        print("Grade: F")
elif score >= 80:
    if attendance >= 80:
        print("Grade: B")
    else:
        print("Grade: F")
elif score >= 70:
    if attendance >= 70:
        print("Grade: C")
    else:
        print("Grade: F")
elif score >= 60:
    if attendance >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
else:
    print("Grade: F")