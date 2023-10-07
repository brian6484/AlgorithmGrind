from collections import deque

n = int(input())
lst = list(int(input()) for _ in range(n))
stack = deque()
ans = [0 for _ in range(n)]
count =0

for i in range(len(lst)-1,-1,-1):
    temp=0
    while stack:
        if stack[-1][0]<lst[i]:
            temp += stack[-1][1] +1
            stack.pop()
        else:
            break
    count+=temp
    stack.append((lst[i],temp))
print(count)