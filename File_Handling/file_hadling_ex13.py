import os 

with open ("notes.txt","r") as src,open ("notes_copy.txt","w") as dst:
    dst.write(src.read())
    