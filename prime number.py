def primeNumber(n):
    if n<=1:
        return "not a prime number"
    for i in range(2,n):
        if n%i==0:
            return "not prime number"
    return "prime number"
n=int(input())
print(primeNumber(n))