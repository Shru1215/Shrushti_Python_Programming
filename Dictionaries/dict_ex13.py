#Create a dictionary of students and marks.Find the student with the lowest marks.

# Create a dictionary of students and marks.
# Find the student with the lowest marks.

d = {}

for i in range(3):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    d[name] = marks

lowest = min(d.values())

for name, marks in d.items():
    if marks == lowest:
        print("Student:", name)
        print("Marks:", marks)