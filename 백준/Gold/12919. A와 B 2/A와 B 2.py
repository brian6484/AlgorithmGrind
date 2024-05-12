s = input().strip()
t = input().strip()

def dfs(s,t):
    if s==t:
        print(1)
        exit()
    if len(s)==len(t):
        return
    if t[-1]=='A':
        dfs(s, t[:-1])
    if t[0]=='B':
        dfs(s,t[1:][::-1])
dfs(s,t)
print(0)