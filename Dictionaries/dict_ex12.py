#Create a dictionary of 5 employees and their salaries.
#Find the total salary paid to all employees.


d = {}
for i in range(5):
     name = input("Enter employee name: ")
     salary = int(input("Enter salary: "))
     d[name] = salary
total = sum(d.values())


print("total salary:",total)
     