import copy,sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)
n = int(input())
board = []

for _ in range(n):
    lst = list(map(int, input().split()))
    board.append(lst)
    
moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
ans = 1
maxVal = max(max(row) for row in board)

def dfs(level, graph, i, j):
    for move in moves:
        next_row, next_col = move[0] + i, move[1] + j
        if 0 <= next_row < n and 0 <= next_col < n:
            if graph[next_row][next_col] > level:
                graph[next_row][next_col] = 0
                dfs(level, graph, next_row, next_col)

for a in range(maxVal):
    tmp = copy.deepcopy(board)
    count = 0
    for i in range(n):
        for j in range(n):
            if tmp[i][j] > a:
                tmp[i][j] = 0
                count += 1
                dfs(a, tmp, i, j)

    ans = max(ans, count)

print(ans)