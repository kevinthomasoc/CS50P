sentence = input("Enter your sentence:")
empty = ""
listt = []
for char in sentence:
    listt.append(char)
for i in range(len(listt)):
    if listt[i] == " ":
        listt[i] = "..."
for char in listt:
    empty += char
print(empty)
