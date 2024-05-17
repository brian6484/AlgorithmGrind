from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

def dfs(node, depth):
    if node == b:
        print(depth)
        exit(0)
    for child in graph[node]:
        if not visited[child]:
            visited[child] = True
            dfs(child, depth + 1)

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = defaultdict(list)

for _ in range(m):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)

visited = [False] * (n + 1)
visited[a] = True

dfs(a, 0)
print(-1)