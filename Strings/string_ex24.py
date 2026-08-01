# write a program that replaces all vowels in a string with *

a = input("Enter a string: ")

for  vowel in "aeiouAEIOU":
      a = a.replace(vowel,"*")  
print(a)
    