class Student:
    college_name = "MIT" # class variable 
    # It is shared by all student objects.

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome to", self.college_name)

    def get_marks(self):
        return self.marks


s1 = Student("Karan", 99)

s1.welcome()
print(s1.get_marks())