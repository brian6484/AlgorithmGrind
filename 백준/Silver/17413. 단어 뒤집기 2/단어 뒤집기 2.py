hola = input()
ans = ''
tmp = ''
flag = False

for i in range(len(hola)):
    if hola[i] == '<':
        if len(tmp)>0:
            ans+=tmp[::-1]
            tmp=''
        flag = True
        ans += '<'
    elif hola[i] == '>':
        flag = False
        ans += '>'
    else:
        if flag:
            ans += hola[i]
        else:
            if hola[i] == ' ' or hola[i] == '<':
                tmp = tmp[::-1]
                ans += tmp
                ans += ' '
                tmp = ''
            else:
                tmp += hola[i]

ans += tmp[::-1]
print(ans)