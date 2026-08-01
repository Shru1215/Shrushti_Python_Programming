# take a string as input 
# if it starts with a vowel , convert the whole string to uppercase
# otherwise convert it into lowecase
# then convert it into a list of characters 
# and print the list in reverse order.

s =input("enter a string:")

for vowel in "aeiouAEIOU":
    if s[0] ==  vowel :
        s = s.upper()
else:
      s = s.lower()

b = list(s)
b.reverse()
print(b)