number = int(input("Enter a number to find out if its negative or positive"))

if number < 0:
    print(str(number) + " is negative")
elif number > 0:
    print(str(number) + " is positive")
else:
    print("number is zero")
