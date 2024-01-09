import sys
import heapq

input=sys.stdin.readline
n = int(input())
lst = []

for _ in range(n):
    a, b = map(int, input().split())
    lst.append([a, b])

lst.sort(key=lambda x: x[0])
room = [lst[0][1]]
heapq.heapify(room)

for i in range(1, n):
    start, end = lst[i]
    
    if room[0] <= start:
        heapq.heappop(room)
    heapq.heappush(room, end)

print(len(room))
