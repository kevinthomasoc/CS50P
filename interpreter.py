equation = input("Enter an expression:")
x, y, z = equation.split()
x = int(x)
y = str(y)
z = int(z)
if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x-z))
elif y == "*":
    print(float(x*z))
elif y == "/":
    print(float(x/z))

    
