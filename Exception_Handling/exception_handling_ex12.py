# WAP to input 2 numbers and print 
# 1.the first number is greater if the first number is larger
# 2. the second number is greater otherwise


try:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))

    if a > b:    
     print("First number is greater")
    else:
     print("Second number is greater")

except ValueError:
    print("Invalid input")

finally:
    print("Done")
    
