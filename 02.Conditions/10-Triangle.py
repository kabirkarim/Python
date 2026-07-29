# Develop a program that takes three integers as input, representing the sides of a triangle. Use nested if-else
# statements to determine and print whether the triangle is valid (based on the triangle inequality theorem) and
# what type it is (equilateral, isosceles, scalene, or right-angled).
# Input three sides
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

# Check if triangle is valid
if (a + b > c) and (a + c > b) and (b + c > a):
    print("The triangle is valid.")

    if a == b == c:
        print("Type: Equilateral Triangle")
    else:
        if a == b or b == c or a == c:
            print("Type: Isosceles Triangle")
        else:
            if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
                print("Type: Right-Angled Triangle")
            else:
                print("Type: Scalene Triangle")
else:
    print("The triangle is not valid.")