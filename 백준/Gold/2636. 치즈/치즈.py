import sys
from collections import deque

n,m=  map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))


ans=[]

moves = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs():
    queue =deque()
    visited[0][0]=True
    queue.append((0,0))
    count=0
    while queue:
        cur_x,cur_y= queue.popleft()
        for move in moves:
            next_x,next_y = move[0]+cur_x, move[1]+cur_y
            if 0<=next_x<n and 0<=next_y<m and not visited[next_x][next_y]:

                if graph[next_x][next_y]==0:
                    queue.append((next_x,next_y))
                    visited[next_x][next_y]=True
                elif graph[next_x][next_y]==1:
                    graph[next_x][next_y]=0
                    visited[next_x][next_y]=True
                    count+=1
    ans.append(count)
    return count
time=0
while True:
    time+=1
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = bfs()
    if count==0:
        break
print(time-1)
print(ans[-2])