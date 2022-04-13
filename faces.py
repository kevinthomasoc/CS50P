sentence = input("Enter a sentence:")

def switch(text):
    a = text
    if ((":)" in a) == True):
        b = a.replace(":)", "🙂")
        a = b

    if ((":(" in a) == True):
        b = a.replace(":(", "🙁")
        a = b

    return a


print(switch(sentence))
