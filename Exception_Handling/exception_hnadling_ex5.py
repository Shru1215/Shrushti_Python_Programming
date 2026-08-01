def divide(x):      # function
    try:
        r = 5 / x
        return r
    except ZeroDivisionError:
        return "Not divisible by 0"

# main program
try:
    x = int(input("Enter integer: "))
    y = divide(x)

    if isinstance(y, float):
        a = 10 + y
        print("a =", a)
    else:
        print(y)

except ValueError:
    print("Not a valid input")

