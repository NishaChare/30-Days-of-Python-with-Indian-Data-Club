#With basic input validation
length = float(input("Length: "))
width = float(input("Width: "))

if length > 0 and width > 0:
    print("Area:", length * width)
else:
    print("Length and width must be positive numbers.")
