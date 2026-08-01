#Create two dictionaries of cricket players and their runs.Merge them.If a player exists in both
#  dictionaries, add their runs.

d1 = {}
d2 ={}

print("first dictionary:")

for i in range(3):
    name = input("Enter player name: ")
    runs = int(input("Enter runs: "))
    d1[name] = runs

print("second dictionary:")

for i in range(3):
    name = input("Enter player name: ")
    runs = int(input("Enter runs: "))
    d2[name] = runs

d = {}

for name in d1:
    if name in d2:
        d[name] = d1[name] + d2[name]
    else:
        d[name] = d1[name]

for name in d2:
    if name not in d1:
        d[name] = d2[name]

print("Merged dictionary:")
print(d)