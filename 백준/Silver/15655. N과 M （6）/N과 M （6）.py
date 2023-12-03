n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    for i in range(start, n):
        if nums[i] not in temp:
            temp.append(nums[i])
            dfs(i + 1)
            temp.pop()

dfs(0)