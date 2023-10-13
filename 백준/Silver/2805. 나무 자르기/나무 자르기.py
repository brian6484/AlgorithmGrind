import sys
input = sys.stdin.readline

n, target = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
left = 0
right = lst[-1]
while left<=right:
    mid = (left+right)//2
    tmp=0
    for a in lst:
        if a>mid:
            tmp+=a-mid
    if tmp>=target:
        left=mid+1
    else:
        right=mid-1
print(left-1)