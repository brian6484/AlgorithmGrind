from collections import Counter

hola = input()
dic = Counter(hola)
tmp = ''

count = 0
mid = ''

for key, val in sorted(dic.items()):
    if val % 2 == 1:
        count += 1
        mid = key
        if count == 2:
            print("I'm Sorry Hansoo")
            exit()

    tmp += key * (val // 2)

print(tmp + mid + tmp[::-1])