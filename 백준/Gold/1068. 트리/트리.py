import math
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n=int(input())
lst = list(map(int,input().split()))
m=int(input())
count=0

def dfs(delete,lst):
    lst[delete]=-2
    for i in range(n):
        if lst[i]==delete:
            dfs(i,lst)
dfs(m,lst)
for i in range(n):
    if lst[i]!=-2:
        if i!=-1 and i not in lst:
            count+=1
print(count)