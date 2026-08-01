# Take input of a stence
# convert how many time "a" appears
# If count is between  2 -3 replace "a" with "o"
# #Else convert sentence to title case ,find the result

s = input("Enter a sentence: ")

a = s.count('a')

if a >=2 and a <= 3:
    print(s.replace('a', 'o')) 
else:
    print(s.title()) 
