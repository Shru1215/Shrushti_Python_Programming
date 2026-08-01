# write a function check() which accept a number from calling program and return message as odd
#  or even in calling program input number call function check passing number as paramter 
#display result as odd or even

def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

try:
    num = int(input("enter a number:"))

    r = check(num)
    print(r)

except ValueError:
    print("Invalid Salary")
