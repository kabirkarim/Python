# Write a multiplication table of a number n.
num=int(input("Enter a number to get it's table: "))
for i in range(1,11):
    print(f"{num} x {i} = {i*num}")