#count the number of non-vowel character in a string

a =input("enter a string:")
count = 0

for ch in a:
    if ch in "aeiouAEIOU":
        continue
    count = count + 1

print("Number of non-vowel characters =", count)