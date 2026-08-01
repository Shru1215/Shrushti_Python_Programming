#Count the frequency of each character in a 


a = input("Enter a string: ")

while len(a) > 0:
    ch = a[0]
    print(ch, "=", a.count(ch))
    a = a.replace(ch, "")