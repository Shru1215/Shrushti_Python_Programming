# 2. Write a program to cube every number in a list using map() and a lambda.



n = [1,2,3,4,5]

cube = list(map(lambda x: x**3, n))

print(cube)