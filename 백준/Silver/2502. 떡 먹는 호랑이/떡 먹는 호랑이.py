d, k = map(int, input().split())
dp = [(0, 0) for _ in range(d + 1)]
dp[1] = (0, 1)
dp[2] = (1, 0)

for i in range(3, d + 1):
    dp[i] = (dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1])

a, b = dp[d]

for x in range(1, 100001):
    for y in range(1, 100001):
        if a * y + b * x == k:
            print(x)
            print(y)
            break
    else:
        continue
    break