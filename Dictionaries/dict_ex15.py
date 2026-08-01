#Create a dictionary of students and marks.Ask the user for a student's name.If found, remove the
#  student from the dictionary.Print the updated dictionary.


d = {}
for i in range(4):
    name = input("enter a student name:")
    marks = int(input("enter marks of a student :"))
    d [ name] = marks 

name = input("enter the students name to remove :")

if name in d:
    del d[name]
    print("Student removed.")
else:
    print("Student not found.")


print("Updated dictionary:")
print(d)