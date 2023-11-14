import sys 
input = sys.stdin.readline
ans = 0
dic = {}
lst = []

while True:
    inp = input().strip()
    if not inp:
        break
    dic[inp] = dic.get(inp, 0) + 1
    ans += 1

for key, value in dic.items():
    lst.append([key, round((value / ans)*100, 4)])

lst.sort(key=lambda x: x[0])
for a,b in lst:
    print('%s %.4f' %(a,b))