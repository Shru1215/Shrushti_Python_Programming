# Take a list of integers as input. create one set containing values that appears only once and 
# another set conatining values that appears more then once .

l =[]

for i in range(4):
 a = int(input("enter an integer "))
 l.append(a)

 o = set()
 m = set()

 for i in l:
   if l.count(i) == 1:
        o.add(i)
 else:
      m.add(i)

print("onces = ",o)
print("more =", m)