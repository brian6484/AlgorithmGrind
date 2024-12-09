import sys,bisect
input = sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))
ans = list(sorted(set(lst)))
hola = []
for i in lst:
    hola.append(bisect.bisect_left(ans,i))
print(*hola)