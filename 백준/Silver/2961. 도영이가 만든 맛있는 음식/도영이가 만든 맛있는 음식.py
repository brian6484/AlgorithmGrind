import sys
input = sys.stdin.readline
n = int(input())
lst = []
ans = int(10e9)

for _ in range(n):
    lst.append(list(map(int, input().split())))

for mask in range(1, 1 << n):
    p, s = 1, 0
    for i in range(n):
        if (mask & (1 << i)) != 0:
            p *= lst[i][0]
            s += lst[i][1]

    ans = min(ans, abs(p - s))

print(ans)