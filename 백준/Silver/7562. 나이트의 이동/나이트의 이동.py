import sys
input = sys.stdin.readline
from collections import deque

t= int(input())
for _ in range(t):
    n=int(input())
    start_x,start_y = map(int,input().split())
    end_x,end_y = map(int,input().split())

    moves = [[1,2],[2,1],[1,-2],[-1,2],[-1,-2],[2,-1],[-2,1],[-2,-1]]
    count = [[-1 for _ in range (n)] for _ in range(n)]
    def bfs():
        queue =deque()
        queue.append((start_x,start_y))
        # count = [[0 for _ in range (n)] for _ in range(n)]
        count[start_x][start_y]=0
        while queue:
            cur_x,cur_y= queue.popleft()
            if cur_x==end_x and cur_y==end_y:
                return count[cur_x][cur_y]
            for move in moves:
                next_x = move[0]+cur_x
                next_y = move[1]+cur_y

                if 0<=next_x<n and 0<=next_y<n and count[next_x][next_y]==-1:
                    count[next_x][next_y]= count[cur_x][cur_y]+1
                    queue.append((next_x,next_y))
    # print(count)
    val = bfs()
    print(val)