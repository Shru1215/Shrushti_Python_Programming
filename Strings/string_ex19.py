# check whether the string is a palindrome 

a = input("enter a string:")

b = a[::-1]

if a == b:
     print("palindrome")
else:
     print("not a palindrome")