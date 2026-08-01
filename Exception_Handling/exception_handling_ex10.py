# Raise ValueError for 0 or positive inputs using 'as' , also handle system raised exception for
#  ValueError

try:
    num = int(input("Enter a negative number: "))

    if num >= 0:
        raise Exception("0 or positive numbers are not allowed")
    print(num)

except ValueError :
    print("invalid input")
