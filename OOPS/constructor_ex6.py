class Doctor:
    def __init__(self, name, department, experience, salary, hospital):
        self.name = name
        self.department = department
        self.experience = experience
        self.salary = salary
        self.hospital = hospital
d1 = Doctor("Karan", "Cardiology", 10, 100000, "Apollo")
d2 = Doctor("Arjun", "Neurology", 8, 90000, "Fortis")

print(d1.name, d1.department, d1.experience, d1.salary, d1.hospital)
print(d2.name, d2.department, d2.experience, d2.salary, d2.hospital)                                            