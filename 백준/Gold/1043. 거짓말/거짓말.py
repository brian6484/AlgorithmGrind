import sys
input = sys.stdin.readline
per, par = map(int, input().split())
banned = list(map(int, input().split()))[1:]
party = []
parent = [i for i in range(per + 1)]

for ban in banned:
    parent[ban] = 0
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

for _ in range(par):
    tmp = list(map(int, input().split()))[1:]
    for i in range(len(tmp) - 1):
        union(tmp[i], tmp[i + 1])
    party.append(tmp)

count = 0
flag = False

for p in party:
    for element in p:
        if find_parent(element) == 0:
            flag = True
            break

    if not flag:
        count += 1
    else:
        flag = False

print(count)
