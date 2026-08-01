class Bank:
    def __init__(self, name, acc_no, bank_name, balance):
        self.name = name
        self.acc_no = acc_no
        self.bank_name = bank_name
        self.balance = balance

b1 = Bank("Karan", "1234567890", "SBI", 10000)
b2 = Bank("Arjun", "0987654321", "HDFC", 5000)

print(b1.name, b1.acc_no, b1.bank_name, b1.balance)
print(b2.name, b2.acc_no, b2.bank_name, b2.balance)