from collections import defaultdict
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    graph = defaultdict(list)
    n, m = map(int, input().split())
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False for _ in range(n + 1)]

    def dfs(node, count):
        visited[node] = True
        for n in graph[node]:
            if not visited[n]:
                count = dfs(n, count + 1)
        return count

    val = dfs(1, 0)
    print(val)