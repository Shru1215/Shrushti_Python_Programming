# using lambada function

a = [2,3,6,5,10,14]
c = list(filter(lambda x: x%2==0,a))
print(c)


a = [2,3,6,5,10,14]
c = list(filter(lambda x: x%2==0,range(10)))
print(c)