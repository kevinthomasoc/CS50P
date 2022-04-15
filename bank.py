greeting = input("Enter a greeting:")
greeting = (greeting.lower()).strip()
if ("hello" in greeting) == True:
    print("$0")
elif ("h" in greeting) == True and (greeting.index("h")) == 0:
    print("$20")
else:
    print("$100")
