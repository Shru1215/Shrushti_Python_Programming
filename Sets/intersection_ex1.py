 #Take two lists of integers as input .Find and display the elements that are common for both lists.

l = []
s = []

for i in range(4):
    a = int(input("Enter first integer: "))
    l.append(a)

for i in range(4):
    b = int(input("Enter second integer: "))
    s.append(b)

a = set(l)
b = set(s)

print(a & b)