# using a while loop find the sum of digits of a number entered by the user (ex: 1234 gives 1+2+3+4=10)

num = int(input("Enter a number: "))

sum = 0

while num > 0:
    digit = num % 10
    sum +=   digit
    num = num // 10

print("Sum of digits =", sum)