#write a recursive function to count the number of digits in a number 

def count(n):
    if n == 0:
        return 0
    return 1 + count(n //10 )

print(count(123))