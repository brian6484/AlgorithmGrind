import math

string = input()
n = int(string)

if n < 9:
    print(n + 1)
    exit()
elif n == 9:
    print(11)
    exit()
else:
    length = len(string)
    if length % 2 == 0:
        left, right = string[:length // 2], string[length // 2:]
        if int(right) < int(left[::-1]):
            print(left + left[::-1])
        else:
            up_left = str(int(left) + 1)
            if len(up_left) == len(left):
                print(up_left + up_left[::-1])
            elif len(up_left)>len(left):
                print(up_left + up_left[::-1][1:])
    else:
        left, right = string[:length // 2], string[length // 2 + 1:]
        mid = string[length // 2]
        if int(right) < int(left[::-1]):
            print(left + mid + left[::-1])
        else:
            if int(mid) == 9:
                up_left = str(int(left) + 1)
                if len(up_left) == len(left):
                    print(up_left + "0" + up_left[::-1])
                elif len(up_left)>len(left):
                    print(up_left + up_left[::-1])
            else:
                print(left + str(int(mid) + 1) + left[::-1])