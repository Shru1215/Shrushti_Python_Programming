# write a python programming to create a dict containing the names of 5 employees and their salaries.
#ASK the user to enter an employees name if the employee exists display the salary otherwise display
#"employee not found".Then allow the user to update the salary of an existing employee.


d = {}

for i in range (5):
    name = input("enter employee name:")
    salary = int (input("enter salary:"))
    d[name] = salary

name = input("Enter employee name to search: ")

if name in d:
    print("Salary:",d[name])
    new_salary = int(input("Enter new salary: "))
    d.update({name: new_salary})
    print("Updated dictionary:")
    print(d)

else:
    print("employee not found")
    


