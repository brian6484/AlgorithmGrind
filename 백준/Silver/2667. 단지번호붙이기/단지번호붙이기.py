n=int(input())
graph=[]
for _ in range(n):
    split = input().strip()
    graph.append(list(map(int,split)))

moves=[[1,0],[-1,0],[0,1],[0,-1]]
ans=[]
count=0
def dfs(x,y):
    global count
    count+=1
    for move in moves:
        next_x, next_y = move[0]+x, move[1]+y
        if 0<=next_x<n and 0<=next_y<n:
            if graph[next_x][next_y]==1:
                graph[next_x][next_y]=0
                dfs(next_x,next_y)

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            graph[i][j]=0
            dfs(i,j)
            ans.append(count)
            count =0

ans.sort()
print(len(ans))
for i in ans:
    print(i)