import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
hola = input()
count = 0
i=0
tmp=0
while i<len(hola):
    if hola[i:i+3]=='IOI':
        tmp+=1
        i+=2
        if tmp==n:
            count+=1
            tmp-=1
    else:
        i+=1
        tmp=0

print(count)