import sys
input = sys.stdin.readline
t=int(input())
for _ in range(t):
    n = int(input())
    lst=[]
    for _ in range(n):
        a,b = map(int,input().split())
        lst.append([a,b])
    lst.sort(key=lambda x:x[0])
    ans=1
    maxA=lst[0][1]
    for i in range(len(lst)):
        if lst[i][1]<maxA:
            ans+=1
            maxA=lst[i][1]
    print(ans)