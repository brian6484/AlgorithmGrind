import sys
input = sys.stdin.readline

n=int(input())
lst = list(map(int,input().split()))
m=int(input())
hola = list(map(int,input().split()))
lst.sort()

def binary_search(num):
    left,right=0,n-1
    while left<=right:
        mid = left+(right-left)//2
        if lst[mid]==num:
            print(1)
            return
        elif num>lst[mid]:
            left=mid+1
        else:
            right=mid-1
    print(0)

for i in hola:
    binary_search(i)