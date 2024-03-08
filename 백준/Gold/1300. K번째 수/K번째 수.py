def count_valid(num, n):
    count = 0
    for i in range(1, n + 1):
        count += min(num // i, n)
    return count

def binary_search_smallest_element(n, m):
    left, right = 1, n * n

    while left < right:
        mid = left + (right - left) // 2
        count = count_valid(mid, n)
        
        if count >= m:
            right = mid
        else:
            left = mid + 1

    return left 

n = int(input())
m = int(input())

result = binary_search_smallest_element(n, m)
print(result)
