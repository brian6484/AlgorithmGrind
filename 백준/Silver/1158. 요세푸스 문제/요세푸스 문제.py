import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst=[i for i in range(1,n+1)]
ans=[]
num=0
for _ in range(n):
    num += m-1
    if num>=len(lst):
        num%=len(lst)
    ans.append(str(lst.pop(num)))
print("<",", ".join(ans)[:],">", sep='')
