a = 10
b = 20

def add():
    a = 30
    b = 40
    print("func " , a+b)

    add()
    print("global", a+b)