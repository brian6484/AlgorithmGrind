import heapq,sys
input = sys.stdin.readline
n = int(input())
m = int(input())
distance = [int(10e18) for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

x, y = map(int, input().split())
heap = []
heapq.heapify(heap)
heapq.heappush(heap, [0, x])
def dijkstra(cost, node):
    while heap:
        cur_cost, cur_node = heapq.heappop(heap)
        if distance[cur_node] < cur_cost:
            continue
        for hola in graph[cur_node]:
            next_cost,next_node = hola
            if cur_cost+next_cost < distance[next_node]:
                distance[next_node] = cur_cost+next_cost
                heapq.heappush(heap, (cur_cost+next_cost, next_node))
distance[x]=0
dijkstra(0,x)
print(distance[y])
