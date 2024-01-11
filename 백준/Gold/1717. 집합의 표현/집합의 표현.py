import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]  # Initialize parent array

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

for _ in range(m):
    a, node1, node2 = map(int, input().split())
    if a == 0:
        union(node1, node2, parent)
    else:
        if find_parent(node1, parent) != find_parent(node2, parent):
            print("NO")
        else:
            print("YES")
