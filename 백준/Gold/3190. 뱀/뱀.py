from collections import deque

n = int(input())
m=int(input())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b]=2
k = int(input())
dicMove = dict()
for _ in range(k):
    x,c = input().split()
    dicMove[int(x)] = c

moves = [[0,1],[1,0],[0,-1],[-1,0]]
queue =deque()
queue.append((1,1))
ans = 0
x,y=1,1
graph[x][y]=1
direction=0

def turn(alpha):
    global direction
    if alpha=='L':
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4

while True:
    ans+=1
    x+=moves[direction][0]
    y+=moves[direction][1]
    if 0<x<=n and 0<y<=n:
        if graph[x][y]==2:
            queue.append((x,y))
            graph[x][y]=1
            # tail_x, tail_y = queue.popleft()
            # graph[x][y]=0
            if ans in dicMove:
                turn(dicMove[ans])
        elif graph[x][y]==0:
            graph[x][y]=1
            queue.append((x,y))
            tail_x, tail_y = queue.popleft()
            graph[tail_x][tail_y]=0

            if ans in dicMove:
                turn(dicMove[ans])
        else:
            break
    else:
        break
print(ans)
