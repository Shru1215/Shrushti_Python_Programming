# nested
try:
    a=int(input("enter an integer"))
    b=int(input("enter an integer"))
    # division
    c=a/b
    print("result =",c)

    #multiplication
    m=a*b
    print("multiplication =",m)

    # addition
    s=a+b
    print("addition =",s)

     #substraction
    t=a-b
    print("subtraction =",t)

    #modulus
    k=a%b
    print("modulus =",k)

except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print("result =",c)
finally:
    print("done")