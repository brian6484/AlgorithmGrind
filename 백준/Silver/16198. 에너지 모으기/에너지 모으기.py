n= int(input())
lst = list(map(int,input().split()))

hola = 0

def dfs(ans):
    global hola
    if len(lst)==2:
        hola = max(hola,ans)
        return

    for i in range(1, len(lst)-1):
        k = lst[i]
        ans+=lst[i-1]*lst[i+1]
        del lst[i]
        dfs(ans)
        lst.insert(i,k)
        ans-=lst[i-1]*lst[i+1]
dfs(0)
print(hola)