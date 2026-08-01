# check if value is integer find its square root only if it is true

import math
try:
    num =int(input("enter an integer:"))
    print( math.sqrt(num))

except ValueError:
    print("Invalid input")

