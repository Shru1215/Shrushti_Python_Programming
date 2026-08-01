#If it starts with "a" to "A"convert it to uppercase(startswith()) 
#Else find the result after converting it to lowercase.

u = "Apple"

if u.startswith("a") or u.startswith("A"):
    print(u.upper())
else:
    print(u.lower())