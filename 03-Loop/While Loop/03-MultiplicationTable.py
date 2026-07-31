# Write a multiplication table of a number n.
num=int(input("Enter a number: "))
count=1
while count<=12:
    print(f"{num} x {count} = {num*count}")
    count+=1
