import sys
input = sys.stdin.readline

n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))
check=set()

for i in range(n):
    for j in range(i,n):
        check.add(lst[i]+lst[j])
ans=0

for k in range(n-1,-1,-1):
    for z in range(k):
        if lst[k]-lst[z] in check:
            ans=max(ans,lst[k])
print(ans)