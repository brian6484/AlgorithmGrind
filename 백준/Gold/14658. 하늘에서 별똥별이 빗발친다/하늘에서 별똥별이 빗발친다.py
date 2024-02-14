import sys
input = sys.stdin.readline

n, m, l, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(k)]
ans = 0

for sx, sy in lst:
    for fx, fy in lst:
        tmp = 0
        minX, minY = min(sx, fx), min(sy, fy)
        for x, y in lst:
            if minX <= x <= minX + l and minY <= y <= minY + l:
                tmp += 1

        ans = max(ans, tmp)

print(k-ans)