import sys
input = sys.stdin.readline

n=int(input())
lst = list(map(int,input().split()))
ans=1

dp1 = [1 for _ in range(n)]
dp2 = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if lst[i]>lst[j]:
            dp1[i]=max(dp1[i], dp1[j]+1)
lst.reverse()
for i in range(n):
    for j in range(i):
        if lst[i]>lst[j]:
            dp2[i]=max(dp2[i], dp2[j]+1)

dp2.reverse()
for i in range(n):
    ans=max(dp1[i]+dp2[i]-1,ans)

print(ans)