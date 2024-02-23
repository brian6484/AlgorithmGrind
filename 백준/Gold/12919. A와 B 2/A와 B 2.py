s = input()
t = input()

def dfs(s, t):
    if len(s) == len(t):
        if s == t:
            print(1)
            exit()
        else:
            return

    if t[-1] == 'A':
        dfs(s, t[:-1])

    if t[0] == 'B':
        dfs(s, t[1:][::-1])

dfs(s, t)
print(0)
