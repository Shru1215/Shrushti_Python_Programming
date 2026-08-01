# raising exceptions with **as**
# 1. raise an exception if the input is not integer

try:
    a=int(input("enter the integer"))
    b=a**5
    print("result =",b)
except:
    print("invalid input,plz input only integers")
finally:
    print("done")