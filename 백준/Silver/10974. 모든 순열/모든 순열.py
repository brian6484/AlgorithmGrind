n = int(input())
lst = [i for i in range(1, n + 1)]
visited = [False for _ in range(n + 1)]
tmp = []

def dfs(tmp):
    if len(tmp) == n:
        print(*tmp)
        return

    for i in lst:
        if not visited[i]:
            tmp.append(i)
            visited[i] = True
            dfs(tmp)
            tmp.pop()
            visited[i] = False

dfs(tmp)