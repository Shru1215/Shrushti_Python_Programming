#Take input as string
#If it startswith "p"  find positions of "o" using find()
#Else check if it is alphanumeric using isalnum(),find approperiate result

s = input("enter a string:")

if s.startswith("p"):
    print("position = ",s.find("o")+1)
    
    
elif s.isalnum():
    print("string is alphanumeric")
else:
    print("string is not alphanumeric")