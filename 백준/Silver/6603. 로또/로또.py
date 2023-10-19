while True:

    tmp = list(map(int, input().split()))
    n = tmp[0]
    lst = tmp[1:]
    ans = []
    if n==0:
        break

    def dfs(i, count):
        if count == 6:
            print(*ans)
            return

        for next in range(i, n):
            ans.append(lst[next])
            dfs(next + 1, count + 1)
            ans.pop()

    dfs(0, 0)
    print()