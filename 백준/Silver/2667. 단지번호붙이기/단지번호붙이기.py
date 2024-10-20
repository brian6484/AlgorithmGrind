import sys
input = sys.stdin.readline

t = int(input())
graph=[]
for _ in range(t):
    graph.append(list(map(int,input().strip())))
moves = [[1,0],[-1,0],[0,1],[0,-1]]
ans=[]
count = 0

def dfs(i,j):
    global count
    count+=1
    graph[i][j]=0
    for move in moves:
        next_x,next_y = move[0]+i,move[1]+j
        if 0<=next_x<len(graph) and 0<=next_y<len(graph[0]) and graph[next_x][next_y]==1:
            dfs(next_x,next_y)

for i in range(t):
    for j in range(len(graph[0])):
        if graph[i][j]==1:
            dfs(i,j)
            ans.append(count)
            count = 0

ans.sort()
print(len(ans))
for i in ans:
    print(i)