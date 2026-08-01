# take a tuple of integers as input find the largest and smallest values and create a list 
# containing all elements that lie strictly between the smallest and largest values.

l = []

for i in range(5):
    a = int(input("Enter a number: "))
    l.append(a)

t = tuple(l)

small = min(t)
large = max(t)

print("Smallest =", small)
print("largest =", large)