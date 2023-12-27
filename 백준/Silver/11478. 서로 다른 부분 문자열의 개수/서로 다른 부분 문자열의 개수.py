hola = input()
check = set()

for i in range(len(hola)):
    for j in range(i + 1, len(hola)+1):
        check.add(hola[i:j])

print(len(check))