class Product:
    def __init__(self, name, product_id, brand, price, rating):
        self.name = name
        self.product_id = product_id
        self.brand = brand
        self.price = price
        self.rating = rating

p1 = Product("Laptop", 1234, "Dell", 50000, 4.5)
p2 = Product("Smartphone", 5678, "Samsung", 30000, 4.0)

print(p1.name, p1.product_id, p1.brand, p1.price, p1.rating)
print(p2.name, p2.product_id, p2.brand, p2.price, p2.rating)