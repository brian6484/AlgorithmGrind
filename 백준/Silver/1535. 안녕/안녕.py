import sys
input = sys.stdin.readline
n = int(input())
weights = [0] + list(map(int, input().split()))
happiness = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(101)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(101):
        if weights[i] <= j:
            dp[i][j] = max(dp[i - 1][j - weights[i]] + happiness[i], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][99])