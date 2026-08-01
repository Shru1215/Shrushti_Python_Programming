# 8. Write a program that uses filter() to keep only prime-looking small numbers (2, 3, 5, 7) from 
# 1-10.

r = list(filter(lambda x: x in [2, 3, 5, 7], range(1, 11)))
print(r)