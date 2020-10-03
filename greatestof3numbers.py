x = int(input("Insert first number: "))
y = int(input("Insert second number: "))
z = int(input("Insert third number: "))


if x <= y >= z:
    print(y)
elif y <= x >= z:
    print(x)
elif x <= z >= y:
    print(z)