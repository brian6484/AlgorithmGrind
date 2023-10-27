import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n = int(input())
ori = [input().strip() for _ in range(n)]
change = [input().strip() for _ in range(n)]
dic = defaultdict(list)
ans = 0

for i in range(n):
    dic[ori[i]].append(i)
    i += 1
change.reverse()
tmp = int(10e18)


for i in range(n):
    if dic[change[i]][0] < tmp:
        if dic[change[i]][0]==0:
            ans+=1
            break
        else:
            ans+=1
            tmp = dic[change[i]][0]

print(n-ans)