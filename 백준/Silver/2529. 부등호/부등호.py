n = int(input())
brackets = list(map(str,input().split()))
visited= [False for _ in range(10)]
min_ans=''
max_ans=''
def check(i,j,h):
    if h=='<':
        return i<j
    else:
        return i>j

def dfs(idx,hola):
    global min_ans,max_ans
    if idx==n+1:
        if len(min_ans)==0:
            # since we are iterating from 0 to 9 sequentially the first string that meets the condition is garanteed the smallest
            min_ans=hola
        else:
            max_ans=hola
        return

    for i in range(10):
        if not visited[i]:
            if idx==0 or check(hola[-1],str(i),brackets[idx-1]):
                # if i do hola+=str(i), I need to slice it for backtracking or else it will accumulate
                hola+=str(i)
                visited[i]=True
                dfs(idx+1,hola)
                hola=hola[:-1]
                visited[i]=False
dfs(0,'')
print(max_ans)
print(min_ans)