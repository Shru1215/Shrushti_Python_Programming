# write a python program to input the names and marks of 5 students into a dict where the student
#  names is key and the marks are the value.display the student who scored the highest marks 


d = {}

for i in range(4):
    name = input("enter a name: ")
    marks = int(input("enter marks: ")) 
    d[name] = marks
    print(d)

highest = max(d.values())
for name,marks in d.items():
    if marks == highest:
     print("student who scored the highest marks :",name)
print("marks:", highest)
