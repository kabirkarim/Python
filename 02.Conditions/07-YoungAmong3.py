# If the ages of Ali, Hamza and Basit are input through the keyboard, write a program to determine the youngest of the three
Ali=int(input("Enter Age Of Ali: "))
Hamza=int(input("Enter Age Of Hamza: "))
Basit=int(input("Enter Age Of Basit: "))

# if Ali>Hamza>Basit:
#     print("Basit is the youngest.")
# elif Ali>Hamza<Basit:
#     print("Hamza is the youngest.")
# else:
#     print("Ali is the youngest.")

if Ali<Hamza and Ali<Basit:
    print("Ali is the youngest.")
elif Hamza<Ali and Hamza<Basit:
    print("Hamza is the youngest.")
else:
    print("Basit is the youngest.")
