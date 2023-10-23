import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n,m= map(int,input().split())
lst = list(map(int,input().split()))
for _ in range(m):
    lst.sort(reverse=True)
    val = lst.pop()+lst.pop()
    lst.append(val)
    lst.append(val)
print(sum(lst))