n = int(input())
m = int(input())
hola = input()
count = 0
check = "I" + "OI" * n
length = len(check)

for i in range(m - length + 1):
    if hola[i:i + length] == check:
        count += 1

print(count)