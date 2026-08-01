# write a program to input a students marks and print pass if marks are 35 or above 

try:
    marks =int(input("enter student marks :"))
    if  marks >= 35:
        print("Pass")
    else:
        print("Fail")
except ValueError:
    print("Invalid input ")
finally :
    print("Done")