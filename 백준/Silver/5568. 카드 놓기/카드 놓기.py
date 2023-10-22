n= int(input())
k = int(input())
lst = []
for  _ in range(n):
    lst.append(int(input()))

ans = set()
visited= [False for _ in range(n)]

def dfs(tmp):
    if len(tmp)==k:
        ans.add(int(''.join(map(str,tmp))))
        return

    for i in range(n):
        if not visited[i]:
            tmp.append(lst[i])
            visited[i]=True
            dfs(tmp)
            tmp.pop()
            visited[i]=False
dfs([])
print(len(ans))