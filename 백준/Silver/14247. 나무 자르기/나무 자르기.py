import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
grow = list(map(int, input().split()))
tmp = []

for i in range(n):
    tmp.append((lst[i], grow[i]))

tmp.sort(key=lambda x: x[1])
ans = 0

for i in range(n):
    height, growth = tmp[i][0], tmp[i][1]
    ans += height + i * growth

print(ans)