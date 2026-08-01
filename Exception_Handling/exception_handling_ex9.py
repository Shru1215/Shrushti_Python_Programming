# WAP to input age and print:
# a. eligible to vote if age is 18 or above 
# b. not eligible to vote otherwise

try:
    age = int(input("Enter your age: "))
    if age >= 18:
     print("Eligible to vote") 
    else:
     print("Not eligible to vote")

except ValueError:
    print("Invalid input")
finally :
    print("Done")


