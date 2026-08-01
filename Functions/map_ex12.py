# 11. Write a program to convert a list of Fahrenheit temperatures to Celsius using map()

fahrenheit = [0, 20, 37, 100]

celsius = list(map(lambda f: (f -32) * 9/5, fahrenheit))

print(fahrenheit)