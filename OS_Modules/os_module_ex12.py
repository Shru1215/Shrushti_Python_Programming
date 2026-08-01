# Print only files

import os

for i in os.listdir():
    if os.path.isfile(i):
        print(i)
        