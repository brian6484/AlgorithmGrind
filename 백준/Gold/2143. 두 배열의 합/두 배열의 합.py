from collections import defaultdict
import sys
input=sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

ans = 0
tmp = defaultdict(int)

for i in range(n):
    for j in range(i, n):
        val = sum(a[i:j+1])
        tmp[val] += 1

for i in range(m):
    for j in range(i, m):
        val = sum(b[i:j+1])
        ans += tmp[t - val]

print(ans)