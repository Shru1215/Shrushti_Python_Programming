try:
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))

except ValueError:
    print("Invalid input")

else:
    try:
        c = a / b
        print("Result =", c)

    except ZeroDivisionError:
        print("Cannot divide by zero")