res, tmp = "", ""
while True:
    word = input("Please type in a word: ")
    if word == "end" or word == tmp:
        break
    tmp = word
    res += word + " "
print(res)
