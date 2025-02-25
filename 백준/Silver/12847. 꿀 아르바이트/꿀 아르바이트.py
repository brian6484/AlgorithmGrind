import sys
input =  sys.stdin.readline
n,m = map(int,input().split())
lst = list(map(int,input().split()))
test = lst[:m]
window=sum(lst[:m])

ans = window
for i in range(m,n):
    window = window-lst[i-m]+lst[i]
    ans = max(ans,window)
print(ans)