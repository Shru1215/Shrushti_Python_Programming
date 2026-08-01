import os 

with open("notes.txt","w") as f :
    f.write("line1\nline2\nline3\n")

with open ("notes.txt","r") as f :
    print(f.readline())
    print(f.readline())
    print(f.readline())