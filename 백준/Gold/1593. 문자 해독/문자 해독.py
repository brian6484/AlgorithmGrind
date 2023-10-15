from collections import Counter

n, m = map(int, input().split())
w = str(input().strip())
g = str(input().strip())
check = Counter(w)
start = Counter(g[:n])
ans = 0

for i in range(len(g) - len(w) + 1):
    if check == start:
        ans += 1
    if i + n < len(g):
        start[g[i + n]] += 1
    start[g[i]] -= 1

print(ans)