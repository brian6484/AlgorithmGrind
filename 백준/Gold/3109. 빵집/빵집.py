import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n, m = map(int, input().split())
graph=[list(input().strip()) for _ in range(n)]
count = 0
dy = [1, 1, 1]
dx = [-1, 0, 1]
visited = [[False for _ in range(m)] for _ in range(n)]


def dfs(row, col):
    global count
    visited[row][col] = True
    if col == m - 1:
        count += 1
        return True

    for i in range(3):
        next_x, next_y = row + dx[i], col + dy[i]
        if 0 <= next_x < n and 0 <= next_y < m:
            if graph[next_x][next_y] != "x" and not visited[next_x][next_y]:
                if dfs(next_x, next_y):
                    return True
    return False

for i in range(n):
    dfs(i, 0)

print(count)