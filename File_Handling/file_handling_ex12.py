import os 
with open ("notes.txt") as f :
    text = f.read()
lines = text.splitlines()
words = text.split()
print("lines:",len(lines))
print("lines:",len(words))
print("lines:",len(text))

print("lines:", lines)
print("lines:", words)
print("lines:", text)