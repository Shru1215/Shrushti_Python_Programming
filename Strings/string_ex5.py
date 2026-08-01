# Assign Email-id as 'admin@gmail.com' password as 'admin#1234'
# a. Ask user to input user mail-id and password 
# b. If correct display message as 'login successful' otherwise display correct message like
# 'emailid incorrect','password incorrect'.Both incorrect give maxium 3 attempts ,otherwise display
#  as  'account blockecd'
  
email = "admin@gmail.com"
password = "admin#1234"

attempt = 0

while attempt < 3:
    e = input("Enter Email ID: ")
    p = input("Enter Password: ")

    if e == email and p == password:
        print("Login Successful")
        break

    elif e != email and p == password:
        print("Email ID Incorrect")

    elif e == email and p != password:
        print("Password Incorrect")

    else:
        print("Email ID and Password Incorrect")

    attempt = attempt + 1

if attempt == 3:
    print("Account Blocked")







