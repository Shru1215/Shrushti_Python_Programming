#take a list integers as input .find the second-largest unique number,The list may conatin 
# duplicate values.

l = []


for i in range(5):
    a = int(input("Enter an integer: "))
    l.append(a)


b = set(l)
c =  list(b)

print(c[-2])