n, m = map(int, input().split())
ans = 0

while bin(n).count('1') > m:
    index = bin(n)[2:][::-1].index('1')
    ans += 2**index
    n += 2**index

print(ans)