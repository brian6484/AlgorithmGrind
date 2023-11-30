s = input()
t = input()

while len(t) != len(s):
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]

if t != s:
    print(0)
else:
    print(1)