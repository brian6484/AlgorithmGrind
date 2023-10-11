from collections import deque

def bfs(i, j):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    while queue:
        cur_x, cur_y = queue.popleft()
        for move in moves:
            next_x, next_y = cur_x + move[0], cur_y + move[1]
            if 0 <= next_x < n and 0 <= next_y < m:
                if not visited[next_x][next_y] and graph[next_x][next_y] == 1:
                    graph[next_x][next_y] = 0
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    ans = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] and not visited[i][j]:
                bfs(i, j)
                ans += 1

    print(ans)