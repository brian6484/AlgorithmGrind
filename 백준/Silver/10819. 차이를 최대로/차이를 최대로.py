n = int(input())
lst = list(map(int, input().split()))
ans = 0
visited = [False for _ in range(n)]

def dfs(tmp):
    global ans
    if len(tmp) == n:
        hola = 0
        for i in range(n - 1):
            hola += abs(tmp[i] - tmp[i + 1])
        ans = max(ans, hola)
        return

    for i in range(n):
        if not visited[i]:
            tmp.append(lst[i])
            visited[i] = True
            dfs(tmp)
            visited[i] = False
            tmp.pop()

dfs([])
print(ans)