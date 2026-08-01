# write a recurssive function to print number from 1 to n 

def num(n):
    if n == 0:
        return
    num(n - 1)
    print(n)

num(5)