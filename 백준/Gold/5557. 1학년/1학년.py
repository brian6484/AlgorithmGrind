n = int(input())
lst = list(map(int, input().split()))
dp = [[0 for _ in range(21)] for _ in range(n + 1)]
dp[0][lst[0]] = 1

for i in range(1, n):
    for j in range(21):
        if dp[i - 1][j]:
            if j + lst[i] <= 20:
                dp[i][j + lst[i]] += dp[i - 1][j]
            if j - lst[i] >= 0:
                dp[i][j - lst[i]] += dp[i - 1][j]

target = lst[-1]
print(dp[n - 2][target])
