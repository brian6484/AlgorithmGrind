n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(dp[-1][-1])
            exit()  # Exit the program when the result is found

        val = graph[i][j]

        # down
        if 0 < i + val < n:
            dp[i + val][j] +=  dp[i][j]

        # right
        if 0 < j + val < n:
            dp[i][j + val] +=dp[i][j]