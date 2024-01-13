import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

row, col = map(int, input().split())
visited = [[-1 for _ in range(col)] for _ in range(row)]
graph = [list(map(int, input().split())) for _ in range(row)]
moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

visited[0][0] = -1

def dfs(sx, sy):
    if sx == row - 1 and sy == col - 1:
        return 1
    if visited[sx][sy] != -1:
        return visited[sx][sy]

    count = 0
    for move in moves:
        next_x, next_y = move[0] + sx, move[1] + sy
        if 0 <= next_x < row and 0 <= next_y < col and graph[sx][sy]>graph[next_x][next_y]:
            count += dfs(next_x, next_y)
    visited[sx][sy]=count
    return count

result = dfs(0, 0)
print(result)
