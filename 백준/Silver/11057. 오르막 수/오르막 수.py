n = int(input())
dp = [[0 for _ in range(10)] for _ in range(1001)]

if n == 1:
    print(10)
    exit()
if n == 2:
    print(55)
    exit()

for i in range(10):
    dp[2][i] = 10 - i

for i in range(3, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = sum(dp[i - 1])
        else:
            dp[i][j] = dp[i][j-1] - dp[i - 1][j - 1]
print(sum(dp[n])%10007)