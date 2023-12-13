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
    for i in range(1,len(lst),2):
        if lst[i]!=-1:
            b, c = lst[i], lst[i+1]
            graph[a].append([b, c])


distance = [-1] * (n+1)
distance[1] = 0
dfs(1, distance)

max_val = max(distance)
index = distance.index(max_val)

distance = [-1] * (n+1)
distance[index] = 0
dfs(index, distance)

print(max(distance))