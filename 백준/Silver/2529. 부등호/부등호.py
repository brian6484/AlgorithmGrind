n = int(input())
moves = list(input().split())
lst = [i for i in range(10)]
visited = [False for _ in range(len(lst))]
max_tot = -1
min_tot = 100
ans = []

def dfs(tmp):
    global max_tot, min_tot, ans
    if len(tmp) == n + 1:
        flag = False
        left = tmp[0]
        for i in range(1, n + 1):
            bracket = moves[i - 1]
            right = tmp[i]
            if bracket == '<':
                if left < right:
                    left = right
                else:
                    flag = True
                    break
            else:
                if left > right:
                    left = right
                else:
                    flag = True
                    break
        if not flag:
            val = ''.join(map(str, tmp))
            ans.append(int(val))
            return
        else:
            return

    for i in range(len(lst)):
        if not visited[i]:
            tmp.append(lst[i])
            visited[i] = True
            dfs(tmp)
            tmp.pop()
            visited[i] = False

dfs([])
ans.sort()
changed=''
val=ans[0]
if len(str(val))<n+1:
    changed = '0'*(n+1-len(str(val))) + str(val)
else:
    changed = ans[0]


print(ans[-1])
# print(ans[0])
print(changed)