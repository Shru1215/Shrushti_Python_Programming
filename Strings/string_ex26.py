# write a python program to add'ing at the end of a given string(length should be at least 3) . if
# the given string already ends with 'ing' add 'ly' instead.if the string length of a given string
#  is less then 3,leave it unchanged.

a = input("enrter a string:")
i = len(a) 
if  i < 3:
    print(a)
elif a.endswith("ing"):
     print(a +'ly')
else:
       print(a + 'ing')