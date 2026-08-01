# write a python program to take input for 3*3 matrix and display the matrix row by rwo 

l = []


for i in range(3):
      t = []
      for j in range(3):
        a = int(input("Enter a number: "))
        t.append(a)
      l.append(t)

for e in l:
    print(*e)