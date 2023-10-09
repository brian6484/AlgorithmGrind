import math
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int,input().split()))
def look_left(index):
    count =0
    tmp = int(10e9)
    for i in range(index-1,-1,-1):
        slope = (lst[index]-lst[i])/(index-i)
        if slope<tmp:
            count+=1
            tmp = slope

    return count

def look_right(index):
    count = 0
    tmp = -int(10e9)
    for i in range(index+1,n):
        slope = (lst[index]-lst[i])/(index-i)
        if slope >tmp:
            count+=1
            tmp= slope

    return count

ans= [0 for _ in range(n)]


for i in range(n):
    count1 = look_left(i)
    count2 = look_right(i)
    ans[i]= count1+count2

print(max(ans))