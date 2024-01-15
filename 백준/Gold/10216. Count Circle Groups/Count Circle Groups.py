import math,sys
input = sys.stdin.readline

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

t = int(input())
for _ in range(t):
    n = int(input())
    lst = []
    parent = [i for i in range(n)]
    
    for _ in range(n):
        a, b, c = map(int, input().split())
        lst.append([a, b, c])

    for i in range(n - 1):
        for j in range(i, n):
            x1, y1, r1 = lst[i]
            x2, y2, r2 = lst[j]
            if math.sqrt((x1 - x2)**2 + (y1 - y2)**2) <= r1 + r2:
                union(i, j, parent)

    check = set()
    ans = 0
    for i in range(n):
        par = find_parent(i, parent)
        if par not in check:
            ans += 1
            check.add(par)

    print(ans)