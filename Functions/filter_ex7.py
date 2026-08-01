# 4. Write a program to filter out all words shorter than 4 letters from a list of words.


words = ["hi", "hello", "sun", "tree", "apple", "orange"]

r = list(filter(lambda x: len(x) >= 4, words))

print(r)