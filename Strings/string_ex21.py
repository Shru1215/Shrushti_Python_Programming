# Write a program that takes a sentence and capitalizes
# the first letter of every word without using title()

a = input("Enter a sentence: ")

r = ""

for i in range(len(a)):
    if i == 0:
        r = r + a[i].upper()
    elif a[i-1] == " ":
        r = r + a[i].upper()
    else:
        r = r + a[i]

print(r)



