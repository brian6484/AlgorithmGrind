t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.reverse()
    tmp = lst[0]
    profit = 0
    
    for i in range(1, n):
        if lst[i] < tmp:
            profit += tmp - lst[i]
        else:
            tmp = lst[i]
    
    print(profit)
