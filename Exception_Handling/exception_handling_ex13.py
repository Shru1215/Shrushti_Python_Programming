# WAP to input charcter and print uppercase letter if the character is an uppercase alphabet or 
# not an upper ketter otherwise

try:
    ch = input("Enter a character: ")
    if len(ch) != 1:
        raise Exception("Please enter only one character.")

    if ch.isupper():
        print("Uppercase letter")
    else:
        print("Not an uppercase letter")

except Exception as e:
    print(e)