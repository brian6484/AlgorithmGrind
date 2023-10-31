n, m, a = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(input().rstrip()))

ans = 0
moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = [[False for _ in range(m)] for _ in range(n)]

def dfs(x, y, count):
    global ans
    if x == 0 and y == m - 1:
        if count == a:
            ans += 1
        return
    if count>a:
        return

    for move in moves:
        next_x = move[0] + x
        next_y = move[1] + y
        if 0 <= next_x < n and 0 <= next_y < m:
            if not visited[next_x][next_y] and graph[next_x][next_y] != 'T':
                visited[next_x][next_y] = True
                count += 1
                dfs(next_x, next_y, count)
                visited[next_x][next_y] = False
                count -= 1
visited[n - 1][0]=True
dfs(n - 1, 0, 1)
print(ans)