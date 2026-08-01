# 
import os 
print(os.getcwd())
f = open ("notes.txt","w")
f.write("Hello,this is python text file")
f.close()