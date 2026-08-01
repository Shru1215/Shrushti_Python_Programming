import os 

with open("notes.txt","r") as f :
    print(f.read(4))
    f.seek(3) # pointer
    print(f.read(4))