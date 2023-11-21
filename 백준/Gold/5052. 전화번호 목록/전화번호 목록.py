import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    lst = []

    for _ in range(n):
        lst.append(input().rstrip())

    # Sorting a list of strings lexicographically
    lst.sort()
    flag=False
    for i in range(1, len(lst)):
        if lst[i].startswith(lst[i - 1]):
            
            flag=True
            break
    if flag:
        print("NO")
    else:
        print("YES")