from collections import deque

n = input()
tmp = ''
queue = deque()
ans = 0
flag = True

for i in n:
    if i.isdigit():
        tmp += i
    else:
        if tmp:
            queue.append(int(tmp))
            tmp = ''
        queue.append(i)

if tmp:
    queue.append(int(tmp))

while queue:
    i = queue.popleft()
    if isinstance(i, int):
        if flag:
            ans += i
        else:
            ans -= i
    elif i == '-':
        flag = False

print(ans)