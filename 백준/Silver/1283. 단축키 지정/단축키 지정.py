n = int(input())
dic = {}
dic[' ']=1

for _ in range(n):
    lst = input().split()
    flag=False
    for i in range(len(lst)):
        if lst[i][0].lower() not in dic:
            dic[lst[i][0].lower()] = 1
            lst[i] = "[" + lst[i][0] + "]" + lst[i][1:]
            print(" ".join(lst))
            flag=True
            break
    if flag:
        continue
    ant=False
    hola = " ".join(lst)
    for i in range(len(hola)):
        if hola[i].lower() not in dic:
            dic[hola[i][0].lower()] = 1
            print(hola[:i] + "[" + hola[i] + "]" + hola[i+1:])
            ant=True
            break
    if not ant:
        print(hola)