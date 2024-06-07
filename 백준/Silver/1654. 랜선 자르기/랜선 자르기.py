import sys
input = sys.stdin.readline
k, n = map(int, input().split())
lst=[]
for _ in range(k):
    lst.append(int(input()))


start, end = 1, sum(lst)
ans = 0

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for i in lst:
        tmp += i // mid

    if tmp >= n:
        ans = mid

        start = mid + 1
    else:
        end = mid - 1

print(ans)