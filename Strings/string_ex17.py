# remove the character at index 4 from a string 

a = input("Enter a string: ")
i=len(a) 
if i > 4:
 a = a[:4] + a[5:] 
 print(a)
else:
    print("String is too short.")