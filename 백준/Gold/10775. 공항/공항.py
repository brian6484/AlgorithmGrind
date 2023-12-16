import sys
input = sys.stdin.readline

g=int(input())
p=int(input())
ans=0
parent = [i for i in range(g+1)]

def find(parent, node):
    if parent[node]!=node:
        parent[node]=find(parent,parent[node])
    return parent[node]

def union(node1,node2,parent):
    parent1=find(parent,node1)
    parent2=find(parent,node2)
    parent[parent1]=parent2


for _ in range(p):
    gate = int(input())
    par = find(parent,gate)
    if par==0:
        break
    union(par,par-1,parent)
    ans+=1

print(ans)