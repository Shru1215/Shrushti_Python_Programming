# use list  comprehension to create a list containing all numbers from 1 too 100 that are divisible 
# by both 3 and 5 

l =[x for x in range (1,101) if x%3 == 0 and x%5==0  ]
print(l)