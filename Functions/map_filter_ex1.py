# 12. Write a program combining map() and filter(): double every number, then keep only those 
# above 10.

l = [10,34,4,5]

d = list(map(lambda x: x * 2, l))

r = list(filter(lambda x: x > 10, d))

print(r)