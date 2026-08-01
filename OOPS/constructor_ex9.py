class Mobile:
    def __init__(self, brand,  price):
        self.brand = brand
        self.price = price

    def  display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

m = Mobile("Samsung", 20000)
m.display()