from collections import deque

n = int(input())
lst = list(map(int,input().split()))
stack = deque()
ans = [-1 for _ in range(n)]

for i in range(len(lst)-1,-1,-1):
    while stack:
        if lst[i]<stack[-1]:
            ans[i]=stack[-1]
            break
        else:
            stack.pop()
    stack.append(lst[i])
print(*ans)