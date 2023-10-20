n = int(input())
lst = list(map(int, input().split()))
dp = lst.copy()

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + lst[i])

print(max(dp))