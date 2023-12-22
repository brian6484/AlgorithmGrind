import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
lst = [0] + list(map(int, input().split()))
total_nodes = [1 for _ in range(n + 1)]
parent = [i for i in range(n + 1)]
dp = [0 for _ in range(k+1)]

def find_parent(node, parent):
    if parent[node] != node:
        parent[node] = find_parent(parent[node], parent)
    return parent[node]

def union(node1, node2, parent):
    par1 = find_parent(node1, parent)
    par2 = find_parent(node2, parent)
    if par1 < par2:
        parent[par2] = par1
    else:
        parent[par1] = par2

def knapsack():
    for i in range(1, n + 1):
        if parent[i] != i:
            continue
        for j in range(k - 1, total_nodes[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - total_nodes[i]] + lst[i])

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b, parent)

for i in range(1, n + 1):
    if parent[i] != i:
        par = find_parent(i, parent)
        lst[par] += lst[i]
        total_nodes[par] += total_nodes[i]

knapsack()
print(max(dp))