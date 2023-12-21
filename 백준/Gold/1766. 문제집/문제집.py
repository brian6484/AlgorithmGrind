from collections import defaultdict, deque
import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0 for _ in range(n + 1)]
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

ans = []

def top_sort():
    queue = []
    heapq.heapify(queue)
    
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(queue, i)

    while queue:
        cur = heapq.heappop(queue)
        ans.append(cur)
        for i in graph[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(queue, i)
                

top_sort()

print(*ans)