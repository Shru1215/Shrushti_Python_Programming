# write a program that reverse each word in a sentence but keeps the word order unchanged
#  (eg.,"Python is fun" -> "nohtyP  si nuf")

a = "Python is fun"
w = a.split()

for i in w:
   b = i[::-1] 
   print(b)