# Create a Mobile class with mobile number and balance.
# Create methods to recharge, call and print balance.

class Mobile:
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

    def recharge(self, amount):
        self.balance += amount
        print("Rs.", amount, "recharged")
        print("Balance =", self.get_balance())

    def call(self, amount):
        self.balance -= amount
        print("Rs.", amount, "deducted for call")
        print("Balance =", self.get_balance())

    def get_balance(self):
        return self.balance


m1 = Mobile("9876543210", 100)
m1.recharge(50)
m1.call(20)
m1.recharge(100)