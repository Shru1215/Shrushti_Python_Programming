#Take a sentence as input 
#count how many times the letter "a" appears
#If the count is greater then 2 . replace "a" with "@"
# split the sentence into words,reverse the list,and print it.

s = input("enter a sentence:")

c = s.count("a")

if c >2 :
    s = s.replace("a","@")

b = s.split()
b=b[::-1]
print(b)
