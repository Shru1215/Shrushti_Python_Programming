# write a recurssive function to print number from n to 1

def num(n):
    if n == 0:
        print(1)
        return
    print(n)
    num(n - 1)

num(5)