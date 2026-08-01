# word frequency counter using a dictionary 

text = "the quick brown fox jumps over the lazy dog the fox runs"

words = text.split()
print(words)

d = {}
a= set(words)

for word in a:
    d[word] = words.count(word)


print(d)
