# Take input of a string 
# check if it ends with "ing"
#Else convert to capitalize format print result 

a = input("enter a string:")
if a.endswith('ing'):
    print("string ends with 'ing' ")
else:
    print(a.capitalize())