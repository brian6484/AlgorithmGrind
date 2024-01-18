from collections import deque

lst = []
while True:
    string = input()
    ans = 0
    stack = deque()
    
    if '-' in string:
        break

    for i in range(len(string)):
        hola = string[i]
        if not stack and hola == '}':
            ans += 1
            stack.append('{')
        elif stack and hola == '}':
            stack.pop()
        else:
            stack.append(hola)

    ans += len(stack) // 2
    lst.append(ans)

for i, v in enumerate(lst, start=1):
    print(f"{i}. {v}")
