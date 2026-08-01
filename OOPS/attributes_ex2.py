#create account class with 2 attributes - balance and account number . Create methods for debit , credit and
#  printing the balance.

class Account:
    def __init__(self, balance, acc):
        self.balance = balance
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("RS.", amount, "was debited")
        print("total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("RS.", amount, "was credited")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, "1234567890")
acc1.debit(1000)
acc1.credit(5000)
acc1.credit(2000)
acc1.debit(3000)