n, m = map(int, input().split())
lst = [i for i in range(1, n + 1)]
ans = []

def dfs(parent, count):
    if count == m:
        print(*ans)
        return

    for i in range(parent, n):
        ans.append(lst[i])
        dfs(i + 1, count + 1)
        ans.pop()

dfs(0, 0)
