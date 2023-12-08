import math,sys
input =sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    a, b = map(float, input().split())
    lst.append((a, b))

graph = [[0 for _ in range(n)] for _ in range(n)]
ans = 0

def calc_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if graph[i][j] != 0:
            continue
        from_point = lst[i]
        to_point = lst[j]
        graph[i][j] = calc_distance(from_point[0], from_point[1], to_point[0], to_point[1])
        graph[j][i] = calc_distance(from_point[0], from_point[1], to_point[0], to_point[1])

edges = []

for i in range(n):
    for j in range(i + 1, n):
        cost=math.sqrt((lst[i][0]-lst[j][0])**2 +(lst[i][1]-lst[j][1])**2)
        edges.append((i,j,cost))


edges.sort(key=lambda x: x[2])

parent = [i for i in range(n)]

def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]

def union(node1, node2):
    par1 = find_parent(node1)
    par2 = find_parent(node2)
    if par1 < par2:
        parent[par2] = par1
    else:
        parent[par1] = par2


for edge in edges:
    node1, node2,cost = edge
    if find_parent(node1) != find_parent(node2):
        union(node1, node2)
        ans += cost

print(f"{ans:.2f}")