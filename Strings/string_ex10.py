# Take input of a string 
# if it ends with "ing" (endswith()) convert it to captialize format
#Else convert it to title case
#Find the result 

p = input("Enter a string: ")

if p.endswith('ing'):
    print(p.capitalize())
else:
    print(p.title())