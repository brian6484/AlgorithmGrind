import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
ans = 0

def count_eggs(lst):
    global ans
    count=0
    for i in lst:
        if i[0]<=0:
            count+=1
    ans=max(ans,count)


def dfs(seq,lst):
    global ans
    if seq==n:
        count_eggs(lst)
        return
    if lst[seq][0]<=0:
        dfs(seq+1,lst)
        return

    check = True
    for i in range(n):
        if seq==i:
            continue
        if lst[i][0]>0:
            check=False
            break
    if check:
        count_eggs(lst)
        return

    for i in range(n):
        if i==seq:
            continue
        if lst[i][0]<=0:
            continue
        lst[seq][0] -= lst[i][1]
        lst[i][0] -= lst[seq][1]
        dfs(seq+1,lst)
        lst[seq][0] += lst[i][1]
        lst[i][0] += lst[seq][1]

dfs(0,lst)
print(ans)