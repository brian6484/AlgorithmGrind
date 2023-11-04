import sys
input = sys.stdin.readline
from collections import defaultdict, deque
import math

h=int(input())
lst = list(map(int,input().split()))
ans = defaultdict(list)

def dfs(start,end,level):
    if start==end:
        ans[level].append(lst[start])
        return

    mid = (start+end) //2
    ans[level].append(lst[mid])
    dfs(start,mid-1,level+1)
    dfs(mid+1,end,level+1)

dfs(0,len(lst)-1,0)
for key in ans:
    print(*ans[key])