class Employee:
    def __init__(self, name, emp_id, department,salary,experience):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary
        self.experience = experience

e1 = Employee("Karan", "E001", "IT", 50000, 5)
e2 = Employee("Arjun", "E002", "HR", 40000, 3)

print(e1.name, e1.emp_id, e1.department, e1.salary, e1.experience)
print(e2.name, e2.emp_id, e2.department, e2.salary, e2.experience)