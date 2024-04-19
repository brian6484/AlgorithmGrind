from collections import deque

N, M = map(int, input().split())
queue = deque([(N, 0)])
max_check = 100001
check = [False for _ in range(max_check)]
check[N] = True
ans = [max_check for _ in range(max_check)]

while queue:
    cur_num, cur_count = queue.popleft()
    if cur_num == M:
        print(cur_count)
        exit()
    for i in range(cur_num - 1, cur_num + 2):
        if i == cur_num:
            if 2 * i < max_check and not check[2 * i]:
                queue.append((2 * i, cur_count))
                check[2 * i] = True
        else:
            if 0 <= i < max_check and not check[i]:
                queue.append((i, cur_count + 1))
                check[i] = True