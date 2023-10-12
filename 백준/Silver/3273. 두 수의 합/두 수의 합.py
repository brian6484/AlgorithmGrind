import sys
input = sys.stdin.readline

n=int(input())
lst = list(map(int,input().split()))
m= int(input())
lst.sort()
left,right = 0, len(lst)-1
ans =0
while left<right:
    sum= lst[left]+lst[right]
    if sum==m:
        ans +=1
        left+=1
        right-=1
    elif sum>m:
        right-=1
    else:
        left+=1
print(ans)
