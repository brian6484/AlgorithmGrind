n = int(input())
initial = list(map(int,input().rstrip("\n")))
target = list(map(int,input().rstrip("\n")))

def switch(given, count):
    for i in range(1, n):
        if given[i - 1] == target[i - 1]:
            continue

        count += 1
        for j in range(i - 1, i + 2):
            if j<n:
                given[j] = 1 - given[j]

    if given != target:
        return int(1e9)
    else:
        return count

val1 = switch(initial.copy(), 0)

# Turn on the first bulb this time
initial[0] = 1 - initial[0]
initial[1] = 1 - initial[1]
val2 = switch(initial, 1)

print( min(val1, val2) if min(val1, val2) != int(1e9) else -1 )