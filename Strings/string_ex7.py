#Take input a string
#If it contains only letters (isalpha()),convert it to title case and print it 
#Else convert it to lowercase, find the result

m = input("Enter a string: ")

if m.isalpha():
    print(m.title())
else:
    print(m.lower())