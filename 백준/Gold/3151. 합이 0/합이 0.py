from bisect import bisect_left
import sys

input =sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

ans = 0

def search(left, right, cur_index):
    global ans
    while left < right:
        if lst[left] + lst[right] + lst[cur_index] > 0:
            right -= 1
        else:
            if lst[left] + lst[right] + lst[cur_index] == 0:
                if lst[left] == lst[right]:
                    ans += right - left
                else:
                    leftmost_idx_of_right_val = bisect_left(lst, lst[right])
                    ans += right - leftmost_idx_of_right_val + 1
            left += 1

for i in range(len(lst) - 2):
    search(i + 1, len(lst) - 1, i)

print(ans)