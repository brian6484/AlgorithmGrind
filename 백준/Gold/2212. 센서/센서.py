import sys
input = sys.stdin.readline
n=int(input())
m=int(input())
lst = list(map(int,input().split()))
if n==1:
    print(0)
    exit()
lst.sort()
tmp = []
carry=0
for i in range(1,n):
    tmp.append(lst[i]-lst[i-1])
tmp.sort(reverse=True)
for i in range(m-1):
    carry+=tmp[i]
ans = lst[-1]-lst[0]-carry
print(ans)