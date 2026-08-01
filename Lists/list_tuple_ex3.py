# take a list and a tuple of integers as input remove a elements from the list that are also
#  present in tuple and display the final  list
 
l = []

for i in range(5):
    a = int(input("Enter list element: "))
    l.append(a)

t = []

for i in range(5):
    b = int(input("Enter tuple element: "))
    t.append(b)

t = tuple(t)

for i in l:
    for j in t:
          if i == j:
           l.remove(i)

print("Final List:", l)