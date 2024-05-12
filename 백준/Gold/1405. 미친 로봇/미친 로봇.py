lst = list(map(int, input().split()))
visited = [[False for _ in range(50)] for _ in range(50)]
n = lst[0]
prob=[]
total = 1
for i in range(1,5):
    if lst[i]!=0:
        total *=n
    prob.append(lst[i]/100)
ans = 0

moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
visited[25][25] = True

def dfs(row, col, count, p, check):
    global ans, n, prob
    if check == n:
        if count == n:
            ans += p
        return

    for i in range(4):
        next_row, next_col = moves[i][0] + row, moves[i][1] + col
        if not visited[next_row][next_col]:
            visited[next_row][next_col] = True
            dfs(next_row, next_col, count + 1, p * prob[i], check + 1)
            visited[next_row][next_col] = False
        else:
            continue
            # dfs(next_row, next_col, count, p * prob[i], check + 1)
            # visited[next_row][next_col] = False

dfs(25,25,0,1,0)
print(ans)