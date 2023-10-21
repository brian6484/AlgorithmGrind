import sys
input = sys.stdin.readline
from collections import defaultdict, deque

f,s,g,u,d = map(int,input().split())
moves = [u,-d]
flag = False
visited= [False for _ in range(f+1)]
def bfs():
    queue=deque()
    queue.append((s,0))
    visited[s]=True
    global flag
    while queue:
        cur_x,cur_cost=queue.popleft()
        if cur_x==g:
            flag = True
            return cur_cost
        for move in moves:
            next_x = cur_x+move
            if next_x==cur_x:
                continue
            if 1<=next_x<=f and not visited[next_x]:
                queue.append((next_x,cur_cost+1))
                visited[next_x]=True

ans = bfs()
if flag:
    print(ans)
else:
    print("use the stairs")