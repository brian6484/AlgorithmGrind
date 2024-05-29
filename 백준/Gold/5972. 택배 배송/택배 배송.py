import heapq
from collections import defaultdict

N, M = map(int, input().split())
infinity = float('inf')
distances = [infinity] * (N + 1)
graph = defaultdict(list)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A,C))

distances[1] = 0
heap = []
heapq.heapify(heap)
heapq.heappush(heap, (0, 1))

def dijkstra():
    while heap:
        current_cost, current_city = heapq.heappop(heap)
        if current_cost > distances[current_city]:  # Skip processing if we find a longer path
            continue
        for next_city, next_cost in graph[current_city]:
            new_cost = current_cost + next_cost
            if new_cost < distances[next_city]:
                distances[next_city] = new_cost
                heapq.heappush(heap, (new_cost, next_city))

dijkstra()

print(distances[N])