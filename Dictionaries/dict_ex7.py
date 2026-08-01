# write a python program to input the name of 6 products and their prices into dictionary then :
# 1. display all products costing more then 500
# 2. Find the costliest product
# 3. display the average price of all products 

d = {}

for i in range (6):
    name = input("enter product name:")
    price = int (input("enter product prices:"))
    d[name] = price

for product,price in d.items():
        if price >500:
          print(product,price)

high = 0
costlist = ""

for  product, price in d.items():
      if price > high:
        high = price
        costliest_product = product

print("Costliest product:", costliest_product)
print("Price:", high)

total = 0

for product, price in d.items():
    total += price

average = total / len(d)

print("Average price:", average)


#highest = max(d.values())

#for product, price in d.items():
 #   if price == highest:
  #      print("\nCostliest product:", product)
   #     print("Price:", price)

# Average price
#total = sum(d.values())
#average = total / len(d)

#print("Average price:", average)





