n=int(input())
brackets=list(map(str,input().split()))
visited=[False for _ in range(10)]
min_ans,max_ans=0,0
ans=[]

def check(i,j,h):
    if h=='<':
        return i<j
    else:
        return i>j

def dfs():
    global ans,min_ans,max_ans
    if len(ans)==n+1:
        if min_ans==0:
            min_ans = ''.join(map(str,ans))
        else:
            max_ans = ''.join(map(str,ans))
        return

    for i in range(10):
        if not visited[i]:
          if not ans or check(ans[-1],i,brackets[len(ans)-1]):
              ans.append(i)
              visited[i]=True
              dfs()
              visited[i]=False
              ans.pop()

dfs()
print(max_ans)
print(min_ans)