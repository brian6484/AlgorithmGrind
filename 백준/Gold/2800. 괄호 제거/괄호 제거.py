from itertools import combinations
from collections import deque


hola = list(input())
check = set()
stack=deque()
idx = []

for i in range(len(hola)):
    if hola[i]=='(':
        stack.append(i)
    elif hola[i]==')':
        idx.append([stack.pop(),i])
for i in range(len(idx)):
    for comb in combinations(idx,i+1):
        tmp=hola[:]
        for x,y in comb:
            tmp[x],tmp[y]='',''
        check.add("".join(tmp))
for i in sorted(list(check)):
    print(i)