import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for left in range(n - i):
        right = left + i

        if left == right:
            dp[left][right] = 1
        elif lst[left] == lst[right]:
            if left + 1 == right:
                dp[left][right] = 1
            else:
                if dp[left + 1][right - 1]:
                    dp[left][right] = 1

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(dp[a - 1][b - 1])