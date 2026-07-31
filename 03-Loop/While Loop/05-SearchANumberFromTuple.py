# search for a number x in the tuple
# using loop
num=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter a number to find that it is in the tuple or not: "))
index=0
found=False
while index!=len(num):
    if(num[index] == x):
        found=True
        break
    index+=1
if(found==True):
     print(f"{x} found at index: {index+1}.")
else:
     print(f"{x} not found in tuple.")