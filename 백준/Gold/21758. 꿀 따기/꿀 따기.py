n = int(input())
lst = list(map(int, input().split()))
front, back = [0 for _ in range(n)], [0 for _ in range(n)]
for i in range(n):
    if i == 0:
        continue
    front[i] = lst[i] + front[i - 1]
    back[n - 1 - i] = lst[n - 1 - i] + back[n - i]

ans = 0
# Bee bee honey
for i in range(1, n - 1):
    bee1 = front[n - 1] - lst[i]
    bee2 = front[n - 1] - front[i]
    ans = max(bee1 + bee2, ans)

# Honey bee bee
for i in range(n - 2, 0, -1):
    bee1 = back[0] - lst[i]
    bee2 = back[0] - back[i]
    ans = max(bee1 + bee2, ans)

# Bee honey bee
for i in range(1, n - 1):
    bee1 = front[i]
    bee2 = back[i]
    ans = max(bee1 + bee2, ans)

print(ans)