import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

t = int(input())

def find_parent(node, parent, dic):
    while node != 0:
        dic[node] = 1
        node = parent[node]
    return dic

for _ in range(t):
    n = int(input())
    parent = [0 for i in range(n + 1)]

    for _ in range(n-1):
        a, b = map(int, input().split())
        parent[b] = a

    x, y = map(int, input().split())
    dicX = find_parent(x, parent, {})
    
    while True:
        if y in dicX:
            print(y)
            break
        y = parent[y]