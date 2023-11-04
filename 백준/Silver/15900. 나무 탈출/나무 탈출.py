import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())

graph = defaultdict(list)
dist = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
visited = [False for _ in range(n + 1)]

# Stack for iterative DFS
stack = [1]  # Start with the root node

while stack:
    node = stack.pop()
    visited[node] = True

    for a in graph[node]:
        if not visited[a]:
            dist[a] = dist[node] + 1
            stack.append(a)

for i in range(2, len(dist)):
    if len(graph[i]) == 1:
        count += dist[i]

if count % 2 == 0:
    print("No")
else:
    print("Yes")