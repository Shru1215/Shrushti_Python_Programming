


def divide(a, b):      # function
    c = a / b
    return c

# main program
a = 5

try:
    b = int(input("Enter integer: "))

    try:
        c = divide(a, b)
        print(c)

    except ZeroDivisionError:
        print("Cannot divide by 0")

except ValueError:
    print("Not a valid input")