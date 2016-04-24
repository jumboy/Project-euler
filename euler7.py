def prime(n):
    for i in range(2,int(n**(0.5))+1):
        if n%i == 0:
            return False
counter = 6
n = 13
while counter < 10001:
    n += 1
    if prime(n) != False:
        counter += 1
print(n)
