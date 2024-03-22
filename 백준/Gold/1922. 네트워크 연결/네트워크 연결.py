from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, a, b])
    graph[b].append([c, b, a])

heap = graph[1]
heapq.heapify(heap)

ans = 0
visited = [False for _ in range(n + 1)]
visited[1] = True

while heap:
    c, a, b = heapq.heappop(heap)
    if not visited[b]:
        visited[b] = True
        ans += c
        for hola in graph[b]:
            next_c, next_a, next_b = hola
            if not visited[next_b]:
                heapq.heappush(heap, hola)

print(ans)
