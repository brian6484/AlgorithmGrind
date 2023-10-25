import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n, m = map(str, input().strip().split())

if len(n) != len(m):
    print(0)
    exit()

count = 0
for i in range(len(n)):
    if n[i] == m[i]:
        if n[i] == '8':
            count += 1
    else:
        break

print(count)