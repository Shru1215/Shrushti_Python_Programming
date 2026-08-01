# Take input of a string 
# Remove spaces using strip().
# If the string is lowercase convert to uppercase
#Else convert it to lowercase
#print result using string

d = input("enter a string:")
d = d.strip()
if d.islower():
    print(d.isupper()) 
else:
    print(d.islower()) 