n = int(input())
lst = list(map(int, input().split()))
ans = [0 for _ in range(n)]

# i is person number
for i in range(n):
    count = 0

    # j is index where this person is to be placed in this ans list
    for j in range(n):
        if count == lst[i] and ans[j] == 0:
            ans[j] = i + 1
            break  # Break the loop once the person is placed
        elif ans[j] == 0:
            count += 1

print(*ans)
