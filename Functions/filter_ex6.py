 # 3. Write a program to filter out all negative numbers from a list.

n = [-4,2,-5,1,-9]
c = list(filter(lambda x: x<0 , n))
print(c)