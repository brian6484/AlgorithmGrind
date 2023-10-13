import sys
input = sys.stdin.readline

total, cur = map(int, input().split())
Z = (cur*100 // total)
if Z>=99:
    print(-1)
    exit()
ans = 0
left = 0
right = total

while left <= right:
    mid = left + (right - left) // 2
    new_z = (cur + mid)* 100 // (total + mid)
    if new_z <= Z:
        left = mid + 1
        ans = mid+1
    else:
        right = mid-1

print(ans)
