import sys
input = sys.stdin.readline

n=int(input())
graph = [list(map(int,input().split()) )for _ in range(n)]
graph.sort(key = lambda x: x[1], reverse=True)
ans = graph[0][1]-graph[0][0]
for i in range(1,n):
    if graph[i][1]>=ans:
        ans-=graph[i][0]
    else:
        ans=graph[i][1]-graph[i][0]
print(ans) if ans >= 0 else print(-1)
