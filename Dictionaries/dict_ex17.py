#Create a dictionary of employees and salaries.Find the employee with the second highest salary.

d = {}
for i in range(4):
    name = input("enter a emplyoee name:")
    salary = int(input("enter salary of emplyoee :"))
    d [ name] = salary
    print(d)

highest = max(d.values())

l = []

for salary in d.values():
    if salary != highest:
        l.append(salary)

second = max(l)

for name, salary in d.items():
    if salary == second:
        print("Second highest salary employee:", name)
        print("Salary:", salary)