# write a recursive function to reverse a string 

def string(s):
    if s == "":
        return ""
    return string (s[1:]) + s[0]

s = input("Enter a string: ")
print(string(s))
-