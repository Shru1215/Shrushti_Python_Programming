#write  a function compute () that take salary as parameter and
#calculate bonus as 10% of the salary if salary 27000 else calculate as 8%
#calculate net salary as sum of salary and bonus .
#return the net salary to the calling program . In the calling program input salary and call the
#  function with salary as parameter and print the returned net salary 

def compute(salary):

    if salary > 27000:
        bonus = salary *10 / 100
    else:
        bonus = salary *8 / 100
    net_salary = salary + bonus
    return net_salary


try:
     salary = int(input("Enter Salary: "))
     check = compute(salary)
     print("Net Salary =", check)
    

except ValueError:
    print("Invalid Salary")