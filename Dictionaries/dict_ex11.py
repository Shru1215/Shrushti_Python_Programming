# Write a Python program to input the names and marks of 5 students into a dictionary.
#Display the student who scored the highest marks.

d = {}
for i in range(5):
    name = input("enter a name :")
    marks = int(input("enter a marks:"))
    d[name] = marks
    print(d)

highest = max(d.values())

for name, marks in d.items():
    if marks == highest:
        print("Student:", name)
        print("Marks:", marks)

