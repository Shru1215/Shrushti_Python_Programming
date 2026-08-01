#swap first and last charcters of a string using both positive and negative indexing
a = input("Enter a string: ")

first = a[0]
middle = a[1:5]
last = a[-1]

a = last + middle + first

print(a)