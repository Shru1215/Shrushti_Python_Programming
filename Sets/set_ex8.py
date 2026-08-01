# take 2 sets of integers as input check whether the first set is a subset of the second set . 
# If not display the elements of the first at that are missing from the second set

p = set()
q = set()

for i in range(5):
    a = int(input("Enter element for first set: "))
    p.add(a)

for i in range(5):
    b = int(input("Enter element for second set: "))
    q.add(b)
    
if p.issubset(q):
    print("First set is a subset of the second set.")
else:
    print("Missing elements:", p - q)