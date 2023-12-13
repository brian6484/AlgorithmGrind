from collections import defaultdict
import sys
input = sys.stdin.readline

def dfs(node, distance):
    for neighbor, cost in graph[node]:
        if distance[neighbor] == -1:
            distance[neighbor] = distance[node] + cost
            dfs(neighbor, distance)

n = int(input())
graph = defaultdict(list)

for _ in range(n):
    lst = list(map(int, input().split()))
    a = lst[0]
    lst = lst[1:-1]
    for i in range(len(lst)//2):
        b, c = lst[i*2], lst[i*2+1]
        graph[a].append([b, c])
        graph[b].append([a, c])

distance = [-1] * (n+1)
distance[1] = 0
dfs(1, distance)

max_val = max(distance)
index = distance.index(max_val)

distance = [-1] * (n+1)
distance[index] = 0
dfs(index, distance)

print(max(distance))