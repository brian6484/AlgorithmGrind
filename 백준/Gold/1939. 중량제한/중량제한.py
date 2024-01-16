import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
start,end = map(int,input().split())

def dfs(node,cost):
    if node==end:
        return True
    for next_city,next_cost in graph[node]:
        if not visited[next_city] and next_cost>=cost:
            visited[next_city]=True
            if dfs(next_city,cost):
                return True
    return False

left,right=1,int(10e9)
while left<=right:
    mid = left + (right-left)//2
    visited= [False for _ in range(n+1)]
    visited[start]=True
    if dfs(start,mid):
        left=mid+1
    else:
        right=mid-1
print(left-1)
