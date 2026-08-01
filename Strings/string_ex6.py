# Take input a string
#If it is all lowercase(is lower()), convert it to uppercase and print it.
#Else print "Already not lowercase".

a = input("enter a string:")
if a.islower():
    print(a.upper())
else:
    print("Already not in lowercase")