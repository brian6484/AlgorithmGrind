import sys
from collections import defaultdict

input = sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))
m=int(input())
hola=list(map(int,input().split()))
ans=defaultdict(int)
real_ans=[]
for i in lst:
    ans[i]+=1
for i in hola:
    real_ans.append(ans[i])
print(*real_ans)