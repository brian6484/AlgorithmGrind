import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
tmp = [row[:] for row in graph]
visited = [[False for _ in range(n)] for _ in range(n)]
time = 0
moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(tmp, visited, i, j):
    global sum
    global lst
    visited[i][j] = True
    sum += tmp[i][j]
    lst.append([i, j])
    for move in moves:
        next_x, next_y = i + move[0], j + move[1]
        if 0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y]:
            if l <= abs(tmp[i][j] - tmp[next_x][next_y]) <= r:
                dfs(tmp, visited, next_x, next_y)


while True:
    sum=0
    lst=[]
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(tmp, visited, i, j)
                for point in lst:
                    x, y = point
                    tmp[x][y] = math.floor(sum / len(lst))
                lst=[]
                sum=0
    flag=False
    for i in range(n):
        for j in range(n):
            if tmp[i][j] != graph[i][j]:
                time += 1
                graph = [row[:] for row in tmp]
                flag=True
                break
    if not flag:
        print(time)
        exit()