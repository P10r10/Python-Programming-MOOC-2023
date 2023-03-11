count = 1
while True:
    pin = int(input("PIN: "))
    if pin == 4321:
        break
    print("Wrong")
    count += 1
if count == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {count} attempts")
