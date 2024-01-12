import heapq
import sys
input =sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort(key=lambda x: x[0])
heap = []
heapq.heapify(heap)
ans = 0

for i in range(n):
    day, reward = lst[i]
    if not heap:
        heapq.heappush(heap, reward)
    else:
        if len(heap) < day:
            heapq.heappush(heap, reward)
        else:
            if heap[0] < reward:
                heapq.heappop(heap)
                heapq.heappush(heap, reward)

print(sum(heap))