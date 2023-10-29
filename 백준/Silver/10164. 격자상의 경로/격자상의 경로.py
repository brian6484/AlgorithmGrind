import sys
input = sys.stdin.readline
from collections import defaultdict, deque
import math

n,m,z = map(int,input().split())
graph = [[0 for _ in range(m+1)] for _ in range(n+1)]
count=1
for i in range(1,n+1):
    for j in range(1,m+1):
        graph[i][j]=count
        count+=1
flag = False
row = z//m +1
col = z%m
if z==0:
    flag=True
ans = 0
dx = [1,0]
dy = [0,1]
visited= [[False for _ in range(m+1)] for _ in range(n+1)]
ans_path = []
path =[]

def dfs(x,y):
    global ans
    global flag
    if x==n and y==m and flag==True:
        ans+=1
        ans_path.append(path.copy())
        return
    for i in range(2):
        next_x = dx[i]+x
        next_y = dy[i]+y
        if 1<=next_x<=n and 1<=next_y<=m:
            if not visited[next_x][next_y]:
                if graph[next_x][next_y]==z:
                    flag = True
                visited[next_x][next_y]=True
                path.append([next_x,next_y])
                dfs(next_x,next_y)
                visited[next_x][next_y]=False
                path.pop()
                if flag:
                    flag = False
                if z==0:
                    flag=True


visited[1][1]=False
dfs(1,1)
print(ans)
# print(ans_path)