import re

t = int(input())

for _ in range(t):
    string = input().replace('/n','')
    p = re.compile(r'(100+1+|01)+')
    match = p.fullmatch(string)
    if match:
        print("YES")
    else:
        print("NO")