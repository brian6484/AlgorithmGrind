import math

left, right, digit = map(int, input().split())

def sieve(start, num):
    is_prime = [True for _ in range(num + 1)]
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(num)) + 1):
        if is_prime[i]:
            for multiple in range(i * i, num + 1, i):
                is_prime[multiple] = False

    count = 0

    for i in range(start, num + 1):
        if is_prime[i] and str(digit) in str(i):
            count += 1

    return count

ans = sieve(left, right)
print(ans)
