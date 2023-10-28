import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n,m=map(int,input().split())
ladders={}
snakes={}
for _ in range(n):
    a,b = map(int,input().split())
    ladders[a]=b
for _ in range(m):
    a,b = map(int,input().split())
    snakes[a]=b
visited = [False for _ in range(101)]
count =0

def bfs():
    queue = deque()
    queue.append((1,0))
    visited[1]=True
    while queue:
        cur_pos,cur_cost = queue.popleft()
        if cur_pos==100:
            return cur_cost
        for i in range(6,0,-1):
            next_move = cur_pos+i
            if 1<=next_move<=100:
                if not visited[next_move]:
                    if next_move in ladders.keys():
                        next_move = ladders[next_move]
                    if next_move in snakes.keys():
                        next_move = snakes[next_move]
                    if not visited[next_move]:
                        visited[next_move]=True
                        queue.append((next_move,cur_cost+1))
val = bfs()
print(val)