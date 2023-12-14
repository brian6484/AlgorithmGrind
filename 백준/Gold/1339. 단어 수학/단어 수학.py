import sys
input = sys.stdin.readline

from collections import defaultdict

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
lst = []

for _ in range(n):
    lst.append(input().strip())

dic=defaultdict(int)
for hola in lst:
    length = len(hola)
    for i in hola:
        dic[i]+= 10**(length-1)
        length-=1
sorted_lst = sorted(dic.values(), reverse=True)
ans=0
tmp=9
for val in sorted_lst:
    ans += tmp*val
    tmp-=1
print(ans)