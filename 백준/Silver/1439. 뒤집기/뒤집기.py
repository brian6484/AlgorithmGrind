lst = input()
ans = [0,0]
tmp=lst[0]
ans[int(tmp)]+=1
for i in range(1,len(lst)):
    if lst[i]!=tmp:
        ans[int(lst[i])]+=1
        tmp=lst[i]
    else:
        continue
print(min(ans))