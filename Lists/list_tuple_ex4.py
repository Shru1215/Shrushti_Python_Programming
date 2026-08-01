#take a list ,tuple, and a set of integers as input find and display the numbers that are common 
# to all three conditions

# Take a list, tuple and set as input.
# Find the numbers common to all three.

l = []

for i in range(5):
    a = int(input("Enter list element: "))
    l.append(a)

t = []

for i in range(5):
    a = int(input("Enter tuple element: "))
    t.append(a)

t = tuple(t)

s = set()

for i in range(5):
    a = int(input("Enter set element: "))
    s.add(a)

print("Common elements are:")

for i in l:
    if i in t and i in s:
        print(i)