# Count the number of folders

import os

count = 0

for i in os.listdir():
    if os.path.isdir(i):
        count = count + 1

print("Folders =", count)