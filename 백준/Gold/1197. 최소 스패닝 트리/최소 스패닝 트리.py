import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)
n,m = map(int,input().split())
parent = [i for i in range(n+1)]
edges=[]

for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

def find_parent(node):
    global parent
    if parent[node]!=node:
        parent[node]=find_parent(parent[node])
    return parent[node]

def union(node1,node2):
    par1,par2 = find_parent(node1), find_parent(node2)
    if par1<par2:
        parent[par2]=par1
    else:
        parent[par1]=par2

total=0
for edge in edges:
    cost,a,b = edge
    if find_parent(a)!=find_parent(b):
        union(a,b)
        total+=cost
print(total)
