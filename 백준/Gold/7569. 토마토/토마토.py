import sys
input = sys.stdin.readline
from collections import defaultdict, deque

m,n,h= map(int,input().split())
graph=defaultdict(list)
for a in range(h):
    for b in range(n):
        graph[a].append(list(map(int,input().split())))

moves=[[1,0],[-1,0],[0,1],[0,-1]]
up_down=[1,-1]

visited= [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]

def bfs():
    while queue:
        cur_z,cur_i,cur_j=queue.popleft()
        for move in moves:
            next_i,next_j=move[0]+cur_i,move[1]+cur_j
            if 0<=next_i<n and 0<=next_j<m:
                if graph[cur_z][next_i][next_j]==0:
                    queue.append((cur_z,next_i,next_j))
                    graph[cur_z][next_i][next_j]=graph[cur_z][cur_i][cur_j]+1
        for move in up_down:
            next_z = move+cur_z
            if 0<=next_z<h:
                if graph[next_z][cur_i][cur_j]==0:
                    queue.append((next_z,cur_i,cur_j))
                    graph[next_z][cur_i][cur_j]=graph[cur_z][cur_i][cur_j]+1

queue= deque()
for z in range(h):
    for i in range(n):
        for j in range(m):
            if graph[z][i][j]==1:
                queue.append((z,i,j))

bfs()

time = -69
for z in range(h):
    for i in range(n):
        for j in range(m):
            if graph[z][i][j]==0:
                print(-1)
                exit()
            time = max(time, graph[z][i][j])
print(time-1)