from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n + 1)]
ans = [False for _ in range(n + 1)]
visited[1] = True

def dfs(node, depth):
    if depth == 2:
        return
    for a in graph[node]:
        if not visited[a]:
            ans[a] = True
            visited[a] = True
            dfs(a, depth + 1)
            visited[a] = False
dfs(1,0)
count = 0
for i in ans:
    if i:
        count += 1
print(count)
