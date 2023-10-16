from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs():
    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    queue.append((0, 0))
    flag = False

    while queue:
        cur_x, cur_y = queue.popleft()
        for move in moves:
            next_x, next_y = move[0] + cur_x, move[1] + cur_y
            if 0 <= next_x < n and 0 <= next_y < m:
                if graph[next_x][next_y] == 0 and not visited[next_x][next_y]:
                    queue.append((next_x, next_y))
                    visited[next_x][next_y] = True
                elif graph[next_x][next_y] == 1:
                    count[next_x][next_y] += 1

    for i in range(n):
        for j in range(m):
            if count[i][j] >= 2:
                flag = True
                graph[i][j] = 0

    return flag

time = 0

while True:
    time += 1
    res = bfs()
    if not res:
        break

print(time-1)