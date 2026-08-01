#sum of all the numbers from 0 to n

def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)
n =int(input("enter n: "))
print(sum(n))
    

