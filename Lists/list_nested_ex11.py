# write a program to take 5 numbers as input into a list and print the largest and smallest number

l =[]

for i in range (5):
  a = int(input("enter a number:"))
  l.append(a)


print("largest number",max(l))
print("smallest number",min(l))
