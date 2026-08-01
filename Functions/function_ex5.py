# write a program with a global variable total_sales and a function that updates it using the 
# global keyword after every sale.



def sale(amt):
    global total_sales
    total_sales  +=  amt

total_sales = 0 
sale(500)
sale(200)
sale(100)

print("Totalsales = ", total_sales)