from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(index, distance):
    for hola in graph[index]:
        node, cost = hola
        if distance[node] == -1:
            distance[node] = distance[index] + cost
            dfs(node, distance)

distance = [-1 for _ in range(n + 1)]
distance[1]=0
dfs(1, distance)
index = distance.index(max(distance))

distance = [-1 for _ in range(n + 1)]
distance[index]=0
dfs(index, distance)
index = distance.index(max(distance))

print(distance[index])
