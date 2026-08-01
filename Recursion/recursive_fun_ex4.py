# write a function celsius_to_fahrenheit with a default parameter that converts Celsius to Fahrenheit.

def celsius_to_fahrenheit(c=1):
    f = (c * 9/5) + 32
    return f

print(celsius_to_fahrenheit(100))