import sys

n, m = map(int, input().split())
ori = [list(map(int, list(input()))) for _ in range(n)]
final = [list(map(int, list(input()))) for _ in range(n)]

def reverse(mat, i, j):
    for a in range(i, i+3):
        for b in range(j, j+3):
            if mat[a][b]==0:
                mat[a][b]=1
            else:
                mat[a][b]=0
           

count = 0

if n < 3 or m < 3:
    if ori != final:
        print(-1)
    else:
        print(0)
    exit()

for i in range(n-2):
    for j in range(m-2):
        if ori[i][j] != final[i][j]:
            reverse(ori, i, j)
            count += 1

if ori != final:
    print(-1)
else:
    print(count)