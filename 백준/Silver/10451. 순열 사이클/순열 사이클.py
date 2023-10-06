from collections import defaultdict

n = int(input())
for _ in range(n):
    m = int(input())
    visited = [False for _ in range(m+1)]
    count=0
    # for not making it 0-indexed
    lst = [0] + list(map(int,input().split()))

    def dfs(i):
        visited[i]=True
        node = lst[i]
        if not visited[node]:
            dfs(node)

    for i in range(1,m+1):
        if not visited[i]:
            dfs(i)
            count+=1
    print(count)