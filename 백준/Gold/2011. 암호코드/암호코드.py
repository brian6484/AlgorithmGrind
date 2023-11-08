lst = list(map(int, input().rstrip()))
dp = [0 for _ in range(len(lst) + 2)]
dp[0] = 1
dp[1] = 1

for i in range(len(lst)):
    if 1 <= lst[i] <= 9:
        dp[i + 2] += dp[i + 1]
    
    if i == 0:
        continue

    if 10 <= lst[i - 1] * 10 + lst[i] <= 26:
        dp[i + 2] += dp[i]

print(dp[-1]%1000000)