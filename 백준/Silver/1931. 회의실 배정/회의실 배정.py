n= int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
lst.sort(key = lambda x: (x[1], x[0]))

count =0
prev = 0
for i in lst:
    start,end = i
    if start>=prev:
        count+=1
        prev=end
    else:
        continue
print(count)