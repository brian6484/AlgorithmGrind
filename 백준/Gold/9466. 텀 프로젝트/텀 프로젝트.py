import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111) 

t = int(input())
for _ in range(t):
    n = int(input())
    parent = [0] + list(map(int, input().split()))
    visited = [False for _ in range(n + 1)]

    ans = n

    def dfs(node):
        visited[node] = True
        cycle.append(node)
        if visited[parent[node]]:
            if parent[node] in cycle:
                idx = cycle.index(parent[node])
                return len(cycle[idx:])
        else:
            return dfs(parent[node])

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            cycle_len = dfs(i)
            if cycle_len:
                ans -= cycle_len

    print(ans)