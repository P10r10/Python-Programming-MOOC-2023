print("Please type in integer numbers. Type in 0 to finish.")
count = 0
sum = 0
neg = 0
pos = 0
while True:
    nb = int(input("Number: "))
    if nb == 0:
        break
    count += 1
    sum += nb
    if nb < 0:
        neg += 1
    else:
        pos += 1
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum / count}")
print(f"Positive numbers {pos}")
print(f"Negative numbers {neg}")
