import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
ans = [0 for _ in range(n)]
ans[0] = lst[0]
for i in range(1,n):
    ans[i] += lst[i]+ans[i-1]

m= int(input())
for _ in range(m):
    a,b = map(int,input().split())
    if a>1:
        print(ans[b-1]-ans[a-2])
    else:
        print(ans[b-1])