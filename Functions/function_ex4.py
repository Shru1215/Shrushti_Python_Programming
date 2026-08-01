# write a function max_if_three(a,b,c) that returns the largest of three numbers. 

def max_num(x , y , z):
    if x > y and x > z :
        return x
    elif y > z :
        return y
    else :
        return z

a = 10
b = 25
c = 15    
print(max_num(a , b, c))