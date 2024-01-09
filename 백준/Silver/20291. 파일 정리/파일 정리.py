from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())
dic = defaultdict(int)

for _ in range(n):
    hola = input().strip()
    hola_lst = hola.split(".")
    dic[hola_lst[1]] += 1

for key, val in sorted(dic.items()):
    print(f'{key} {val}')
