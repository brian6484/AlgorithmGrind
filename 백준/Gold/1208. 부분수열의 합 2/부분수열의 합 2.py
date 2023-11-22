import sys
input=sys.stdin.readline
n, s = map(int, input().split())
lst = list(map(int, input().split()))

left_dict, right_dict = {}, {}
ans = 0

def dfs(index, hola, option, _sum):
    if option == "left":
        left_dict[_sum] = left_dict.get(_sum, 0) + 1
    else:
        right_dict[_sum] = right_dict.get(_sum, 0) + 1

    if index == len(hola):
        return

    for i in range(index, len(hola)):
        _sum += hola[i]
        dfs(i + 1, hola, option, _sum)
        _sum -= hola[i]

mid = len(lst) // 2
dfs(0, lst[:mid], "left", 0)
dfs(0, lst[mid:], "right", 0)

for a in left_dict.keys():
    if s - a in right_dict.keys():
        ans += left_dict[a] * right_dict[s - a]

if s == 0:
    ans -= 1

print(ans)
