primes = [2,3,5,7,11,13,17,19]
product = 1 
for p in primes:
    n = 2
    product *= p
    while (p**n < 21):
        product *= p
        n += 1
print(product)
