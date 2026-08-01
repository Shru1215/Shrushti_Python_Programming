#Take 10 integers as input into a list. Remove all duplicate values using a set and display the 
# remaining values in ascending order 


l = []

for i in range(10):
 a = int(input("enter an integers:"))
 l.append(a)

b = set(l)       
c = list(b)    
c.sort()        
print(c)