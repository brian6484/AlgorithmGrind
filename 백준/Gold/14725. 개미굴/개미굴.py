n=int(input())
dic={}

def add(lst,index,dicX):
    if index==len(lst):
        return
    if lst[index] not in dicX:
        dicX[lst[index]]={}
    add(lst,index+1,dicX[lst[index]])
    
for _ in range(n):
    lst =list(map(str,input().split()))
    add(lst[1:],0,dic)
    
def add(lst,index):
    if index==len(lst):
        return
    if dic[lst[index]] not in dic:
        dic[lst[index]]={}
    add(lst,index+1)
    
def printTree(dic,hola):
    for i in sorted(dic.keys()):
        print("--"*hola+i)
        printTree(dic[i],hola+1)

printTree(dic,0)