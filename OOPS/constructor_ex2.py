class Student:
     def __init__(self, name, usn, branch, cgpa):
        self.name = name
        self.usn = usn
        self.branch = branch
        self.cgpa = cgpa

s1 = Student("Karan", "1MS17CS001", "CSE", 9.0)
s2 = Student("Arjun", "1MS17CS002", "CSE", 8.5)
s3 = Student("Ravi", "1MS17CS003", "CSE", 8.0)

print(s1.name, s1.usn, s1.branch, s1.cgpa)
print(s2.name, s2.usn, s2.branch, s2.cgpa)
print(s3.name, s3.usn, s3.branch, s3.cgpa)