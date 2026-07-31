# search for a number x in the tuple using loop
num=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter a number: "))
index=0
for el in num:
    if(el==x):
        print(f"Number found at index: {index}")
    index+=1
    