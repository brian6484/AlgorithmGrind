n = int(input())

def check_palindrome(tmp):
    if tmp == tmp[::-1]:
        return 0

    left, right = 0, len(tmp) - 1
    while left <= right:
        if tmp[left] != tmp[right]:
            res1 = check(left + 1, right, tmp)
            res2 = check(left, right - 1, tmp)
            if res1 or res2:
                return 1
            else:
                return 2
        else:
            left += 1
            right -= 1

    return 0

def check(left, right, tmp):
    while left <= right:
        if tmp[left] != tmp[right]:
            return False
        else:
            left += 1
            right -= 1

    return True

for _ in range(n):
    tmp = input()
    print(check_palindrome(tmp))