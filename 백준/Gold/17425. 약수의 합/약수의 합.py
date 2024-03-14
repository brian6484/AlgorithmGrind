import sys
input = sys.stdin.readline

t = int(input())

def sieve():
    dp = [0 for _ in range(1000001)]
    tmp = [0 for _ in range(1000001)]
    for i in range(1, 1000001):
        # tmp[i] += i
        for multiple in range(i , 1000001,i):
            tmp[multiple] += i
        dp[i] = dp[i - 1] + tmp[i]
    return dp

dp = sieve()
for _ in range(t):
    val = int(input())
    print(dp[val])