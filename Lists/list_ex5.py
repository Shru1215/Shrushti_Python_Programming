# take a string words separated by spaces.
#split it into a list
# remove the first word and the last word 
# join the remaining words using "-" and 
# print thr result 

s = input("enter a string:")

w = s.split()
w.pop(0)
w.pop()

b = '-'.join(w)
print(b)