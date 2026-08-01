#write a function is prime (n)that returns True if n is a prime number else False 

def is_prime(n):
    if n <= 1 :
        return "not prime"

    else:
        for i in range(2 , n):
            if n%i==0:
                return  "not prime"
                break
        if i==n-1:
            return "prime"


n = int(input("Enter a number: "))    

print(is_prime(n))
