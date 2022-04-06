sentence = input("What do you want to say?")
listt = []
empty = ""
for char in sentence:
    listt.append(char)
for i in range(len(listt)):
    if listt[i].isupper():
        listt[i] = listt[i].lower()

for char in listt:
    empty += char
print(empty)
