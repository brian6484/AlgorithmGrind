import sys
input = sys.stdin.readline

n,m=map(int,input().split())
count=1
while m!=n and m>n:
    if m%2==0:
        m//=2
        count+=1
    elif str(m)[-1]== str(1):
        m = int(str(m)[:-1])
        count+=1
    else:
        print(-1)
        exit()
if m<n:
    print(-1)
else:
    print(count)