n = int(input())
lst = []

for _ in range(n):
    lst.append(input())

tmp = lst[0]
ans = 0

for i in range(1, n):
    word = lst[i]
    count = 0
    ori = list(tmp)  # Use list() to create a copy
    for w in word:
        if w in ori:
            ori.remove(w)
        else:
            count += 1

    if count < 2 and len(ori) < 2:
        ans += 1

print(ans)