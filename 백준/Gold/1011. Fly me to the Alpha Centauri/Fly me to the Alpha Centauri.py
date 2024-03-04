t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    distance = y - x

    count = 1
    tmp = 0
    while tmp < distance:
        tmp += (count - 1) // 2 + 1
        count += 1

    print(count - 1)