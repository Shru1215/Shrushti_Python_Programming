#Create a dictionary of students and marks.Display the students in ascending order of marks.

d = {}

for i in range(3):
  name = input("Enter student name: ")
  marks = int(input("Enter marks: ")) 
  d[name] = marks

l = list(d.values())
l.sort()

print("Students in ascending order of marks:")


for mark in  l:
   for name , marks in d.items():
    if marks == mark:
            print(name, marks)