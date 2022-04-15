answer = (input("What is the answer to the Great Question of Life, the Universe, and Everything?")).lower()
answer = answer.strip()
if (answer == "42") or (answer == "forty two"):
    print("Yes")
elif (answer == "forty-two"):
    print("Yes")
else:
    print("No")
