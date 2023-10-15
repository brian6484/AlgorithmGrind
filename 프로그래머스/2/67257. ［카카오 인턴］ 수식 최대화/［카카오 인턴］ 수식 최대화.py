from collections import deque
from itertools import permutations

def solution(expression):
    lst = []
    tmp=''
    for i in expression:
        if i.isdigit():
            tmp+=str(i)
        else:
            lst.append(tmp)
            lst.append(i)
            tmp=''
    lst.append(tmp)

    # for the main logic to be popped
    kirk=deque(lst)

    operations = list(permutations(['-','*','+'],3))

    def calc(x,y,op):
        if op=='*':
            return str(int(x)*int(y))
        elif op=='+':
            return str(int(x)+int(y))
        else:
            return str(int(x)-int(y))

    ans = []

    for oper in operations:
        lst = kirk.copy()
        for op in oper:
            stack=deque()
            while lst:
                tmp = lst.popleft()
                if tmp==op:
                    stack.append(calc(stack.pop(),lst.popleft(),op))
                else:
                    stack.append(tmp)
            lst = stack
        ans.append(abs(int(lst[0])))

    ans.sort()
    return (ans[-1])