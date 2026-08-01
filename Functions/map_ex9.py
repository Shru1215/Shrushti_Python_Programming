# 5. Write a lambda function that returns True if a number is a multiple of 5.


n = [5, 8, 10, 13, 15, 20]

p = list(map(lambda x: x % 5 ==0, n))

print(p)