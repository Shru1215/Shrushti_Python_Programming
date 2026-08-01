class Car:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

c1 = Car("Toyota", "Fortuner", "White", 4500000)
c2 = Car("Hyundai", "Creta", "Black", 1800000)

print("Car 1 Details")
print("Brand:", c1.brand)
print("Model:", c1.model)
print("Color:", c1.color)
print("Price:", c1.price)

print()

print("Car 2 Details")
print("Brand:", c2.brand)
print("Model:", c2.model)
print("Color:", c2.color)
print("Price:", c2.price)