n, m = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(str(1) * gcd(n, m))