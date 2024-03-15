import  sys
input = sys.stdin.readline

n, h = map(int, input().split())
up = [0 for _ in range(h + 1)]
down = [0 for _ in range(h + 1)]

for i in range(n):
    val = int(input())
    if i % 2 == 0:
        down[val] += 1
    else:
        up[val] += 1

# 1-indexed
for i in range(h - 1, 0, -1):
    up[i] += up[i + 1]
    down[i] += down[i + 1]

ans = n
count = 0

for i in range(1, h + 1):
    tmp = down[i] + up[h - i + 1]
    if ans > tmp:
        ans = tmp
        count = 1
    elif ans == tmp:
        count += 1

print(ans, count)