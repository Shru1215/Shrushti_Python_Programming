# count the number of  files

import os

count = 0

for i in os.listdir():
    if os.path.isfile(i):
        count = count + 1

print("Files =", count)