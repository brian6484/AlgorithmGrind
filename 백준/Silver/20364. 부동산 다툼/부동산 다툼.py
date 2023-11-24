import sys
input=sys.stdin.readline

n, m = map(int, input().split())
lst = []

for _ in range(m):
    lst.append(int(input()))

visited=[False for _ in range(n+1)]

for num in lst:
    result=0
    tmp=num
    while num>1:
        if visited[num]:
            result=num
        num//=2
    visited[tmp]=True
    print(result)