ans=0
n,r,c = map(int,input().split())
while n>=1:
    n-=1
    # 1st quadrant
    if r<2**n and c<2**n:
        ans += (2**n) * (2**n) *0
    # 2nd quadrant
    if r<2**n and c>=2**n:
        ans += (2**n) * (2**n) *1
        c-= 2**n
    # 3rd quad
    if r>=2**n and c<2**n:
        r-= 2**n
        ans += (2**n) * (2**n) *2
    # 4th quad
    if r>=2**n and c>=2**n:
        ans += (2**n) * (2**n) *3
        r-= 2**n
        c-= 2**n
print(ans)