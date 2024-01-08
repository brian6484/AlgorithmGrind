import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maxAns = float('-inf')
minAns = float('inf')

def dfs(index, val):
    global maxAns, minAns, add, sub, mul, div  # Declare variables as global

    if index == n:
        maxAns = max(val, maxAns)
        minAns = min(val, minAns)
        return

    if add > 0:
        add -= 1
        dfs(index + 1, val + lst[index])
        add += 1

    if sub > 0:
        sub -= 1
        dfs(index + 1, val - lst[index])
        sub += 1

    if mul > 0:
        mul -= 1
        dfs(index + 1, val * lst[index])
        mul += 1

    if div > 0:  
        div -= 1
        dfs(index + 1, int(val / lst[index]))
        div += 1

dfs(1, lst[0])

print(maxAns)
print(minAns)