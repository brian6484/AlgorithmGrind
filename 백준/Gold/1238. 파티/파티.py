from collections import defaultdict
import heapq,sys
input=sys.stdin.readline

n, m, x = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(node, distance):
    heap = []
    heapq.heappush(heap, (0, node))
    
    while heap:
        cur_cost, cur_node = heapq.heappop(heap)
        
        for next_node, next_cost in graph[cur_node]:
            # optimization to skip unnecessary iterations
            if distance[cur_node] < cur_cost:
                continue
            
            if cur_cost + next_cost < distance[next_node]:
                distance[next_node] = cur_cost + next_cost
                heapq.heappush(heap, (cur_cost + next_cost, next_node))

    return distance

ans = [0] * (n + 1)

for i in range(1, n + 1):
    tmp = [float('inf')] * (n + 1)
    tmp[i]=0
    tmp[0]=0
    hola = dijkstra(i, tmp)
    if i == x:
        for j in range(len(hola)):
            ans[j] += hola[j]
    else:
        ans[i] += hola[x]

print(max(ans))