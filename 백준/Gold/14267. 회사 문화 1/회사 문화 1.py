from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
lst = list(map(int, input().split()))
graph = defaultdict(list)

for i in range(1, n + 1):
    if lst[i-1] == -1:
        continue
    graph[lst[i-1]].append(i)

ans = [0 for _ in range(n + 1)]

def dfs(node):
    global ans
    for child in graph[node]:
        ans[child] += ans[node]
        dfs(child)

for _ in range(m):
    node, no = map(int, input().split())
    ans[node] += no

dfs(1)
print(*ans[1:])