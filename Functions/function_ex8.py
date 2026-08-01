#write a function compute() which accept salary and bonus  percentage to be 2 % calculate bonus 
#a.calculate net salary as sum of salary and bonus return both values of bonus and net slary 
# in calling program input salary and bonus % call function compute passing both salary and bonus
#  percentage .
#display bonus as well as net salary
#again call function compute but passing only salary as parameter, display bonus and net salary .

def compute(salary,bonus_per=2):
    bonus  = salary*bonus_per/100
    net_salary = salary + bonus
    return bonus, net_salary

try:
    salary = int(input("Enter Salary: "))
    bonus_percent = int(input("Enter Bonus Percentage: "))

    bonus, net_salary = compute(salary, bonus_percent)
    print("\nFirst Function Call")
    print("Bonus =", bonus)
    print("Net Salary =", net_salary)

    bonus, net_salary = compute(salary)
    print("\nSecond Function Call")
    print("Bonus =", bonus)
    print("Net Salary =", net_salary)

except ValueError:
    print("Invalid Input")