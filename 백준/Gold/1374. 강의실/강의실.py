import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []
heapq.heapify(heap)
lst = []
count = 0

for _ in range(n):
    num, start, end = map(int, input().split())
    lst.append([start, end])

lst.sort(key=lambda x: x[0])

for i in range(n):
    start, end = lst[i]
    if heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)
    count = max(count, len(heap))

print(count)
