# take a list integers as input .create a tuple conatining only numbers that are divisible by
#  both 2 and 3 .


l = []

for x in range(4):
    a = int(input("Enter an integer: "))
    l.append(a)

t = [x for x in l if x % 2 == 0 and x % 3 == 0] 

t = tuple(t)
print(t) 