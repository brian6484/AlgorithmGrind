
from collections import defaultdict
import sys
input=sys.stdin.readline

N, m = map(int, input().split())
lst = []

for _ in range(m):
    lst.append(int(input()))

dic = defaultdict(list)

for num in lst:
    result=0
    tmp=num
    while num>1:
        if num in dic.keys():
            result=num
        num//=2
    dic[tmp].append(1)
    print(result)