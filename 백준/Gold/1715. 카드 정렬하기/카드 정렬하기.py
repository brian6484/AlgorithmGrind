import heapq
import math
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n=int(input())
heap=[]
heapq.heapify(heap)
ans=0
for _ in range(n):
    heapq.heappush(heap, int(input()))
if n==1:
    print(0)
    exit()
while len(heap)>1:
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    ans += a+b
    heapq.heappush(heap,a+b)
print(ans)