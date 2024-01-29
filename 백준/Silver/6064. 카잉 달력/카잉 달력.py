import sys
input = sys.stdin.readline

def calc(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        else:
            x += m
    return -1

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    result = calc(m, n, x, y)
    print(result)
