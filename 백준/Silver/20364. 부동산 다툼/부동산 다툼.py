import sys
input=sys.stdin.readline

N, m = map(int, input().split())
lst = []

for _ in range(m):
    lst.append(int(input()))

dic = {}

for num in lst:
    result=0
    tmp=num
    while num>1:
        if num in dic.keys():
            result=num
        num//=2
    dic[tmp]=1
    print(result)