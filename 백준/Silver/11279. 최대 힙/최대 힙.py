import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
heapq.heapify(heap)
for _ in range(n):
    m = int(input())
    if m==0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap,-m)