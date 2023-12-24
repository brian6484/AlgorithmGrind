import sys
input = sys.stdin.readline

n,m= map(int,input().split())
lst = list(map(int,input().split()))
lst = set(lst)
lst=sorted(lst)
ans=[]

def dfs():
    if len(ans)==m:
        print(*ans)
        return
    for i in range(len(lst)):
        if len(ans)==0 or ans[-1]<=lst[i]:
            ans.append(lst[i])
            dfs()
            ans.pop()
dfs()