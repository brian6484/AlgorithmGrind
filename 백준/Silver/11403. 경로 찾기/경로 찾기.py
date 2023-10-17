n= int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
# hola = defaultdict(list)
# for i in range(len(graph)):
#     for j in range(len(graph[0])):
#         if graph[i][j]==1:
#             hola[i].append(j)

def dfs(node):

    for i in range(n):
        if graph[node][i]==1 and visited[i]==False:
            visited[i]=True
            dfs(i)

for i in range(n):
    visited= [False for _ in range(n)]
    dfs(i)
    for j in range(n):
        if visited[j]:
            print(1, end=' ')
        else:
            print(0,end=' ')
    print()