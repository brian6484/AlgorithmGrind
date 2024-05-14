from collections import defaultdict


def dfs(n, index, total, expression, lst):
    global dic

    if index == n:
        if total == 0:
            dic[n].append(expression[1:])
        return

    if expression[-2]=='+':
        dfs(n, index + 1, total-int(expression[-1]) + int(expression[-1] + str(lst[index + 1])), expression + " " + str(lst[index + 1]), lst)
    elif expression[-2]=='-':
        dfs(n, index + 1, total+int(expression[-1]) - int(expression[-1] + str(lst[index + 1])), expression + " " + str(lst[index + 1]), lst)
    dfs(n, index + 1, total + lst[index + 1], expression + "+" + str(lst[index + 1]), lst)
    dfs(n, index + 1, total - lst[index + 1], expression + "-" + str(lst[index + 1]), lst)
    
t = int(input())  
ans = [] 
for _ in range(t):
    ans.append(int(input()))  


dic = defaultdict(list)
n = 10  
for i in range(3, 10):
    lst = [i for i in range(0, n + 1)]
    dfs(i, 1, 1, "+1", lst)

for i in ans:
    for val in dic[i]:
        print(val)
    print()