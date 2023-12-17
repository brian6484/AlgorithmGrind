import sys
input = sys.stdin.readline

n=int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
ans=int(10e9)
for i in range(3):
    dp = [[int(10e9) for _ in range(3)] for _ in range(n)]
    dp[0][i] = lst[0][i]
    for j in range(1,n):
        dp[j][0]= lst[j][0] + min(dp[j-1][1],dp[j-1][2])
        dp[j][1] = lst[j][1] + min(dp[j-1][0],dp[j-1][2])
        dp[j][2] = lst[j][2] + min(dp[j-1][0],dp[j-1][1])
    for x in range(3):
        if x!=i:
            ans = min(ans, dp[-1][x])
print(ans)