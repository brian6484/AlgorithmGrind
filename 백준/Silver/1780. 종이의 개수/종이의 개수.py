import sys
input = sys.stdin.readline

n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
ans0=0
ans1=0
ans11=0

def dfs(row, col, z):
    global ans0,ans1,ans11
    check = graph[row][col]
    for i in range(row,row+z):
        for j in range(col,col+z):
            if graph[i][j]!=check:
                for k in range(3):
                    for l in range(3):
                        dfs(row + k*z//3 , col + l*z//3 ,z//3)
                return

    if check==1:
        ans1+= 1
    elif check==0:
        ans0+=1
    else:
        ans11+=1
dfs(0,0,n)
print(ans11)
print(ans0)
print(ans1)