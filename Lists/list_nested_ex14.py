#write a python program to take marks of 3 students in 3 subjects using a nested list and print the
#  total marks of each student.

l=[]

for i in range(3):
      t = []
      for j in range(4):
        a = int (input("enter marks :"))
        t.append(a)

      l.append(t)

for el in l:
     total = 0
for marks in el: 
       total += marks
        
print("total marks =",total)
 