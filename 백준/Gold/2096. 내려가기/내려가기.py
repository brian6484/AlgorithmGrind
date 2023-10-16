import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
maxDp = arr
minDp = arr

for i in range(n - 1):
    graph = list(map(int, input().split()))
    maxDp = [graph[0] + max(maxDp[0], maxDp[1]), graph[1] + max(maxDp), graph[2] + max(maxDp[1], maxDp[2])]
    minDp = [graph[0] + min(minDp[0], minDp[1]), graph[1] + min(minDp), graph[2] + min(minDp[1], minDp[2])]

print(max(maxDp),min(minDp) )