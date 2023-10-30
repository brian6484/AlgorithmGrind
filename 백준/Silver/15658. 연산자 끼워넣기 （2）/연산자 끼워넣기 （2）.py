n=int(input())
num = list(map(int,input().split()))
op = list(map(int,input().split()))

min_tot = int(10e9)
max_tot = -int(10e9)

def dfs(depth,plus,minus,mul,div,total):
    global min_tot, max_tot
    if depth==n:
        min_tot=min(min_tot,total)
        max_tot=max(max_tot,total)
        return

    if plus:
        dfs(depth+1,plus-1,minus,mul,div,total+num[depth])
    if minus:
        dfs(depth+1,plus,minus-1,mul,div,total-num[depth])
    if mul:
        dfs(depth+1,plus,minus,mul-1,div,total*num[depth])
    if div:
        dfs(depth+1,plus,minus,mul,div-1,int(total/num[depth]))

dfs(1,op[0],op[1],op[2],op[3],num[0])
print(max_tot)
print(min_tot)