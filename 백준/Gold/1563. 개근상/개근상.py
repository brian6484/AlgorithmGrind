import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]

def dfs(day, late, absent):
    if late == 2 or absent == 3:
        return 0
    elif day == n:
        return 1

    if dp[day][late][absent] == -1:
        val = (
            dfs(day + 1, late, 0)
            + dfs(day + 1, late + 1, 0)
            + dfs(day + 1, late, absent + 1)
        )
        dp[day][late][absent] = val
        return val
    else:
        return dp[day][late][absent]

print(dfs(0, 0, 0) % 1000000)