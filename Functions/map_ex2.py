#using lambada

def square (x):
    return x**2

n = [1,2,3,4,5]
squared = list(map(lambda  x : x**2, n))
print(squared)

# or 
def square (x):
    return x**2

squared = list(map(lambda  x : x**2, range(1,6)))
print(squared)
