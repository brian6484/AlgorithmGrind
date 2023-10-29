import sys
input = sys.stdin.readline
from collections import defaultdict, deque
import math

n=int(input())
queue = deque(enumerate(map(int,input().split()), start=1))
ans=[]
while queue:
    hola= queue.popleft()
    ans.append(hola[0])
    val = hola[1]
    if val>0:
        queue.rotate(-(val-1))
    else:
        queue.rotate(-val)
print(*ans)