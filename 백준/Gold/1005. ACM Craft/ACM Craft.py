from collections import defaultdict, deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    lst = [0] + list(map(int,input().split()))
    graph = defaultdict(list)
    indegree = [0 for _ in range(n+1)]

    for _ in range(k):
        a,b = map(int,input().split())
        graph[a].append(b)
        indegree[b]+=1

    x = int(input())

    def topo_sort():
        queue = deque()
        ans = []
        cost = [0 for _ in range(n+1)]
        for i in range(1,n+1):
            if indegree[i]==0:
                queue.append(i)
                cost[i] = lst[i]
        while queue:
            cur = queue.popleft()
            if cur == x:
                print(cost[x])
                break
            for i in graph[cur]:
                indegree[i]-=1
                cost[i] = max(cost[i], cost[cur]+lst[i])
                if indegree[i]==0:
                    queue.append(i)
    topo_sort()