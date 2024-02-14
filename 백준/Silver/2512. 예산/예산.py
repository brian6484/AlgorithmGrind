n = int(input())
lst = list(map(int, input().split()))
lst.sort()
hola = int(input())
ans = 0
left = 0
right = max(lst)  

while left <= right:
    mid = (right + left) // 2
    tmp = 0
    for i in lst:
        if i < mid:
            tmp += i
        else:
            tmp += mid

    if tmp <= hola:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)