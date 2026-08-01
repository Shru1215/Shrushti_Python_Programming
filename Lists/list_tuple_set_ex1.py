# Take a list , tuple, and set of integers as input find and display the numbers that are common
#  to all three conditions 

l = []

for i in range(4):
    a = int(input("Enter list element: "))
    l.append(a)

t = []

for i in range(4):
    b = int(input("Enter tuple element: "))
    t.append(b)

t = tuple(t)

s = set()

for i in range(4):
    c = int(input("Enter set element: "))
    s.add(c)


for i in l:
    for j in t:
        for k in s :
            if i ==j and j == k:
             print("common elemnts are:", i )
