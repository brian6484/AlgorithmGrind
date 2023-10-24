import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
lst.sort(key=lambda x:x[0])
start,end = lst[0][0],lst[0][1]
count=0
for i in range(1,n):
    nextX,nextY=lst[i][0],lst[i][1]
    if nextX<=end<=nextY:
        end=max(end,nextY)
    elif start<=nextX<=end and start<=nextY<=end:
        continue
    else:
        count+=end-start
        start=nextX
        end=nextY
count+=end-start
print(count)