from collections import defaultdict, deque
import sys
sys.setrecursionlimit(300000)

N = int(input())
start,end = map(int, input().split())
M = int(input())
graph = defaultdict(list)
ans =[]
visited =[False for _ in range(N+1)]

for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(hola,count):
    if hola==end:
        ans.append(count)
        return
    for next in graph[hola]:
        if not visited[next]:
            visited[next]=True
            dfs(next,count+1)

visited[start]=True
dfs(start,0)
if ans:
    print(ans[0])
else:
    print(-1)
