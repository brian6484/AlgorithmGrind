import sys
input = sys.stdin.readline

from itertools import combinations, permutations

n=int(input())
lst= [ i for i in range(1,n+1)]
graph = [list(map(int,input().split())) for _ in range(n)]
team_size=n//2

teams = list(combinations(lst,team_size))
ans=int(10e18)
for i in range(len(teams)//2):
    pair1 = teams[i]
    pair2 = teams[-i-1]
    val1,val2=0,0
    hola1 = list(combinations(pair1,2))
    hola2 = list(combinations(pair2,2))
    for pair in hola1:
        # make it 0 indexed
        p1,p2 = pair
        val1+=graph[p1-1][p2-1]+graph[p2-1][p1-1]
    for pair in hola2:
        p1,p2=pair
        val2+=graph[p1-1][p2-1]+graph[p2-1][p1-1]
    ans = min(ans, abs(val1-val2))
print(ans)