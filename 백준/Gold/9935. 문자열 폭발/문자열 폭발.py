import sys
x = list(sys.stdin.readline().strip())
M = list(sys.stdin.readline().strip())
m = len(M)
stack = []
for i in x:
    stack.append(i)
    if stack[len(stack)-m:len(stack)] == M: #스택의 끝부터 M의 글자열 크기까지 자른게 M과 같다면
        for _ in range(m): # m의 길이만큼
            stack.pop() # stack에서 꺼내준다!
if stack:
    print(*stack, sep='')
else:
    print("FRULA")
