import sys
d, k = map(int, sys.stdin.readline().split())

for i in range(1, 100000):
    for j in range(1, 100000):
        dp = [0] * (d + 1)
        dp[1] = i
        dp[2] = j

        for l in range(3, d + 1):
            dp[l] = dp[l - 1] + dp[l - 2]

        if dp[-1] == k:

            print(dp[1])
            print(dp[2])
            exit()