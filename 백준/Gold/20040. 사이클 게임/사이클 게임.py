import sys
input=sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n)]

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

for i in range(m):
    a, b = map(int, input().split())
    if find_parent(a, parent) == find_parent(b, parent):
        print(i + 1)
        exit()

    union(a, b, parent)

print(0)
