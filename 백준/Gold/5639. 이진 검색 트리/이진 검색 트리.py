import sys
input = sys.stdin.readline
#recursion error 방지
sys.setrecursionlimit(10**9)
lst = []

while True:
    try:
        lst.append(int(input()))
    except ValueError:
        break

def dfs(lst):
    if len(lst)==0:
        return

    left,right=[],[]
    root = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > root:
            left = lst[1:i]
            right = lst[i:]
            break
    else:
        left = lst[1:]

    dfs(left)
    dfs(right)
    print(root)

dfs(lst)