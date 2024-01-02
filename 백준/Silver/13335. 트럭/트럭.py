from collections import deque

n, w, max_weight = map(int, input().split())
lst = list(map(int, input().split()))

train_queue = deque(lst)
bridge_queue = deque([0 for _ in range(w)])
cur_weight = 0
time = 0

while train_queue or cur_weight > 0:
    cur_node = bridge_queue.popleft()
    cur_weight -= cur_node
    
    if train_queue and cur_weight + train_queue[0] <= max_weight:
        tmp = train_queue.popleft()
        bridge_queue.append(tmp)
        cur_weight += tmp
    else:
        bridge_queue.append(0)

    time += 1

print(time)