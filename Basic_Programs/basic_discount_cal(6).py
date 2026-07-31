# build a discount calculator : given bill amount , apply 5% / 10 % / 20% discount based on amount slabs


bill = 4000

if bill < 1000:
    discount = bill * 5 / 100
elif bill <= 5000:
    
    discount = bill * 10 / 100
else:
    discount = bill * 20 / 100

total_bill = bill - discount

print("Discount =", discount)
print("Total Bill =", total_bill)