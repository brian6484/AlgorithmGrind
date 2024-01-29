dp = [0] + [0 for _ in range(50000)]
n = int(input())
k = 1

while k*k <= n:
    dp[k*k] = 1
    k += 1

for i in range(1, n + 1):
    if dp[i] == 1:
        continue
    j = 1
    while j*j <= i:
        if dp[i] != 0:
            dp[i] = min(dp[i], dp[j*j] + dp[i - j*j])
        else:
            dp[i] = dp[j*j] + dp[i - j*j]
        j+=1

print(dp[n])