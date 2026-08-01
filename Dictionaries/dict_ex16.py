#Create a dictionary of students and marks.Display only the students who scored between 60 and 
# 80 marks.

d = {}
for i in range(4):
    name = input("enter a student name:")
    marks = int(input("enter marks of a student :"))
    d [ name] = marks


print("Students who scored between 60 and 80 marks:")

for name , marks  in d.items():
     if marks >= 60 and marks <= 80 :
          print(name,marks )