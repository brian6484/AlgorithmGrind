import sys
input = sys.stdin.readline

n=int(input())
lst = list(map(int,input().split()))
left,right = 0, len(lst)-1
start = abs(lst[left]+lst[right])
ans = [lst[left],lst[right]]
while left<right:
    sum= lst[left]+lst[right]
    if sum==0:
        print(lst[left],lst[right])
        exit()

    if abs(sum)<start:
        start=abs(sum)
        ans=[lst[left],lst[right]]

    if sum>0:
        right-=1
    else:
        left+=1
print(*ans)