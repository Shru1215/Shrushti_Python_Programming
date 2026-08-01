# Take two lists of integers as input find and display the elements that are common to both lists.

l =[]
s = []

for i in range (4):
    a = int(input("enter first integer"))
    l.append(a)

for i in range (4):
    a = int(input("enter second integer:"))
    s.append(a)

a = set(l)
b = set(s)

print(a&b)