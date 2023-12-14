import sys
input=sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
tmp = float('inf')  # Initialize tmp to positive infinity
ans = 0

for i in range(len(cost)-1):
    if cost[i] < tmp:
        tmp = cost[i]
    ans += distance[i] * tmp

print(ans)