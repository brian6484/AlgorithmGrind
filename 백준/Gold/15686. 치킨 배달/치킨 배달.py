from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
tmp = []
tmp1 = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 2:
            tmp.append((i, j))
        if graph[i][j] == 1:
            tmp1.append((i, j))

combi = combinations(tmp, m)

ans = int(1e9)

for comb in combi:
    hola = 0
    for h in tmp1:
        kirk = 999
        for c in comb:
            kirk = min(kirk, abs(c[0] - h[0]) + abs(c[1] - h[1]))
        hola += kirk
    ans = min(hola, ans)

print(ans)