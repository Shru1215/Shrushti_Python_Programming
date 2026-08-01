# 7. Write a program to find the length of each string in a list using map() and print the result

words = ["apple", "cat", "banana", "cow"]
result = list(map(lambda x: len(x), words))
print(result)