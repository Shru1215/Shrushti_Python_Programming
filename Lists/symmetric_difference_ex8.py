#Take two lists of integers as input.  display the elements that are present in only one
#  of the two lists but not in both 

l = []
s = []


for i in range(4):
     a = int(input("enter first list element:"))
     l.append(a)

for i in range(4):
     b = int(input("enter second list element:"))
     s.append(b)

a = set(l)
b = set(s)

print(a^b) 