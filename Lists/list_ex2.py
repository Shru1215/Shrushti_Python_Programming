# Take a sentence as input 
#remove extra spaces from both sides 
#convert it so each word starts woth a capital letter.
#split it into words and store in a list
#print the list and aslo print the number of words.

s = input("enter a sentence:")
s = s.strip()
s = s.title()
s = s.split()
b = list(s)
print (b)
print("number of words =",len(s))