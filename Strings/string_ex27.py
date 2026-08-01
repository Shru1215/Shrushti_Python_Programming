# WAP to get a string made of the first 2 and last 2 characters of a given string if the string 
# length is less than return the empty string instead.

a = input("enrter a string:")
i =  len(a) 
if  i < 2 :
     print("")
else: 
    print(a[:2]+a[-2:]) 
    print(a)
