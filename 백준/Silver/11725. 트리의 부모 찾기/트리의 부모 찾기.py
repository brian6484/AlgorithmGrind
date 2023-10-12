from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [1] * (n + 1)
visited = [False] * (n + 1)

for i in range(1, n + 1):
    graph[i].sort()

def dfs(i):
    visited[i] = True
    for node in graph[i]:
        if not visited[node]:
            parent[node] = i
            dfs(node)

dfs(1)  # Start the DFS from node 1, assuming it's the root.

for i in parent[2:]:
    print(i)