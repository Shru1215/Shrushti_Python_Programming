#write a program to take input for a 2*2 matrix and store the values in a nested list.

l =[]

for i in range(2):
    t=[]
    for j in range(2):
        a =int(input("enter a number:"))
        t.append(a)

    l.append(t)
    print(l)

