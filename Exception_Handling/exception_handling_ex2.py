# zerodivision error
# raise an error when attemoting division by 0 

try:
    a=int(input("enter an integer ="))
    b=int(input("enter an integer ="))
    c=a/b
    print("result =" , c)
except:
    print("cannot divide by zero")
finally:
    print("done")