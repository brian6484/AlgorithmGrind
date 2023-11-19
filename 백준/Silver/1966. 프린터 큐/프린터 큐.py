from collections import defaultdict, deque
import sys
input = sys.stdin.readline

t= int(input())
for _ in range(t):
    n,m=map(int,input().split())
    lst =list(map(int,input().split()))
    queue =deque()
    for i,v in enumerate(lst):
        queue.append((i,v))
    lst.sort(reverse=True)
    count=0
    while queue:
        i,v= queue.popleft()
        if v==lst[count]:
            count+=1
            if i==m:
                print(count)


        else:
            queue.append((i,v))
