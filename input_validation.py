from math import sqrt

while True:
    nb = int(input("Please type in a number: "))
    if nb == 0:
        break
    if nb < 0:
        print("Invalid number")
    else:
        print(sqrt(nb))
print("Exiting...")
