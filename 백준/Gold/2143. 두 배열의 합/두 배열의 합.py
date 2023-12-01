import sys
from collections import defaultdict

input = sys.stdin.readline
t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

ans = 0
tmp = defaultdict(int)

for i in range(n):
    total_sum = 0
    for j in range(i, n):
        total_sum += a[j]
        tmp[total_sum] += 1

for i in range(m):
    total_sum = 0
    for j in range(i, m):
        total_sum += b[j]
        ans += tmp[t - total_sum]

print(ans)