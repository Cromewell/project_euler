from math import sqrt

def is_prime(m):
    divisors = []
    
    for d in range(1, int(sqrt(m))+1): #it is sufficient to only go <= sqrt(m)
        if(m%d==0):
            divisors.append(d)

    return (len(divisors) == 1) # nur 1 als Teiler (da wir nur bis sqrt(m) gehen)

n = 600851475143
prime_factors = [i for i in range(1, int(sqrt(n))+1) if(is_prime(i) and n%i==0)]

print(prime_factors[-1])