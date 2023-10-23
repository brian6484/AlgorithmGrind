import sys
input = sys.stdin.readline

n = int(input())
lst = [0]
for _ in range(n):
    lst.append(int(input()))
lst.sort()
ans = 0
for i in range(1, n + 1):
    ans += abs(lst[i] - i)
print(ans)