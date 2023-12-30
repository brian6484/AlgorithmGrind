import sys
input = sys.stdin.readline

m,n=map(int,input().split())
lst=list(map(int,input().split()))
left,right=1,max(lst)
ans=0
while left<=right:
    mid = left + (right-left)//2
    total=0
    for i in lst:
        total += i//mid
    if total>=m:
        ans=max(ans,mid)
        left=mid+1
    else:
        right=mid-1
print(ans)