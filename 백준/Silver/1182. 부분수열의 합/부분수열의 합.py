n, s = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0

def dfs(i, sum):
    global ans
    if sum == s and i!=0:
        ans += 1
    for next in range(i, n):
        sum+=lst[next]
        dfs(next+1, sum)
        sum-=lst[next]

dfs(0,0)

print(ans)