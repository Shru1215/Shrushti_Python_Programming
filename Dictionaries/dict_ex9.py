# write a python program to create two dictionaries containing students names and their marks
# merge the 2 dictionaries into a new dict.If  a  student exists in both dictionary keep the
# higher marks as the final value

d1 = {}
d2 = {}

print("first dictionary")
for i in range (4):
    name = input("enter student name:")
    marks = int(input("enter  marks:"))
    d1[name]= marks

print("second dictionary")
for i in range (4):
    name = input("enter student name:")
    marks = int(input("enter  marks:"))
    d2[name]= marks

d = {}

#d1= stu1:10, stu2:20, stu3:30, stu4:40
#d2= stud3:50, stud5:60, stud4:70, stu6:80

#d= stud1:10, stud2:20, stud3:50, stud4:70, stud5:50, stud6:80

for key in d1.keys():
    if key in d2.keys():
        if d1[key] > d2[key]:
            d[key] = d1[key]
        else:
            d[key]=d2[key]
    else:
        d[key] = d1[key]

for key in d2.keys():
    if key not in d1.keys():
        d[key] = d2[key]

print(d)
