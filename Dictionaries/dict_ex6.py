# write a python programming  to input a sentence and create a dictionary that stores each word 
# as the key and the numbers of times it appears in the sentences as the value


text = input("Enter a sentence: ")

d = {}

words = text.split()

for word in words:
    d[word] = d.get(word, 0) + 1

print(d)