import heapq
import sys
input=sys.stdin.readline

n = int(input())
ans = 0
heap = []
heapq.heapify(heap)
lst = []

for _ in range(n):
    money, day = map(int, input().split())
    lst.append([money, day])

lst.sort(key=lambda x: x[1])

for i in lst:
    money, day = i
    heapq.heappush(heap, money)
    if len(heap) > day:
        heapq.heappop(heap)

print(sum(heap))