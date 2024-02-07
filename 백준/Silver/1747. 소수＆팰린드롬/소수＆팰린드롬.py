import math

def sieve(n):
    global is_prime
    is_prime = [True for _ in range(n + 1)]
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False

def palin(num):
    return str(num) == str(num)[::-1]

n = int(input())
sieve(1100001)

for i in range(n, 1100001):
    if is_prime[i] and palin(i):
        print(i)
        exit()