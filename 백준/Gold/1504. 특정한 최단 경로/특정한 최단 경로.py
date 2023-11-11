import heapq
import math
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n,m=map(int,input().split())
graph=defaultdict(list)
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2=map(int,input().split())
heap=[]
heapq.heapify(heap)
tmp = [int(10e18) for _ in range(n+1)]
def dijkstra(node,distance):
    distance[node]=0
    heapq.heappush(heap,(0,node))
    while heap:
        cur_cost,cur_node = heapq.heappop(heap)
        if cur_cost>distance[cur_node]:
            continue
        for hola in graph[cur_node]:
            next_node,next_cost = hola
            if cur_cost+next_cost <distance[next_node]:
                distance[next_node]=cur_cost+next_cost
                heapq.heappush(heap,((cur_cost+next_cost,next_node)))
    return distance
distance1=dijkstra(1,tmp.copy())
distance2=dijkstra(v1,tmp.copy())
distance3=dijkstra(v2,tmp.copy())
min1 = distance1[v1]+distance2[v2]+distance3[n]
min2 = distance1[v2]+distance3[v1]+distance2[n]
if min(min1,min2)>=int(10e18):
    print(-1)
else:
    print(min(min1,min2))