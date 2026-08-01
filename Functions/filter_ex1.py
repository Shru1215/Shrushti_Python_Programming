# 
def filter_odd(item):
    if item %2 == 0 :
        return item
a = [3,22,7,6,10]
b = list(filter(filter_odd,a))
print(b)