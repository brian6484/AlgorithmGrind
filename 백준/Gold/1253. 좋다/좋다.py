n = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 0

for i in range(n):
    left, right = 0, n-1
    while left < right:
        tmp = lst[left] + lst[right]
        if tmp == lst[i]:
            if left == i:
                left += 1
            elif right == i:
                right -= 1
            else:
                ans += 1
                break
        elif tmp > lst[i]:
            right -= 1
        else:
            left += 1

print(ans)