n = int(input())
lst = list(map(int, input().split()))

if n == 1:
    print(sum(lst) - max(lst))
    exit()
else:
    target = []
    for i in range(3):
        target.append(min(lst[i], lst[-1 - i]))

    target.sort()
    ans = 0
    x, y, z = target[0], target[0] + target[1], sum(target)
    ans += z * 4
    ans += y * (n - 1) * 4 + y * (n - 2) * 4
    ans += x * (n - 2) ** 2 * 5 + x * (n - 2) * 4

    print(ans)