# Default Constructor

class Student:
    def __init__(self):
        self.name = "Shrushti"
        self.marks = 90

s1 = Student()

print("Default Constructor")
print(s1.name)
print(s1.marks)

# Parameterized Constructor

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s2 = Student("Karan", 95)
s3 = Student("Arjun", 80)

print("\nParameterized Constructor")
print(s2.name, s2.marks)
print(s3.name, s3.marks)