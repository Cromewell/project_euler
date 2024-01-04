from math import sqrt
from math import pow

def fib(n):
    return (pow((1+sqrt(5))/2, n)- pow((1-sqrt(5))/2, n))/sqrt(5)

sum = 0
n = 1
fib_n = 0.0

while fib_n < 4000000:
    fib_n = int(fib(n))
    
    if(fib_n%2==0):
        sum += fib_n
    n += 1

print(sum)