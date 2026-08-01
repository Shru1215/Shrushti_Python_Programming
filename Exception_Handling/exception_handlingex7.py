# Raise exception manually based on a condition
# Raise an exception when salary is below 10000

try:
    sal = int(input("Enter salary: "))

    try:
        if sal < 10000:
            raise Exception(f"Salary value {sal} cannot be less than 10000")

        bonus = sal * 1
        print("Bonus =", bonus)

    except Exception as x:
        print(x)

except ValueError:
    print("Invalid salary input")