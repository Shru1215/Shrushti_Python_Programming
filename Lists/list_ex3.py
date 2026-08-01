# take a string as input
# if it contains only letters ,convert it to uppercase 
#otherwise ,replace all digit with *
# convert the final string into a list of characters and print it 


a = input("enter a string:")
if a.isalpha():
   a = a.upper()
else:
   for ch in "0123456789":
       a = a.replace(ch,"*")  
b = list(a)
print(b)