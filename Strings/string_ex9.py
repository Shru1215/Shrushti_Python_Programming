#Take input of string 
#If it is in uppercase (isupper()) convert it to lowercase 
#Else convert it using swapcase(),Find the result.

s = input("enter a string:")
if s.isupper():
     print(s.lower())           
else:
     print(s.swapcase())