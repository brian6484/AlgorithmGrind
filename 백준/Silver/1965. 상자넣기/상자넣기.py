n = int(input())
lst = list(map(int, input().split()))
ans = [0 for _ in range(n)]

def lis(nums):
    n = len(nums)
    if n == 0:
        return 0  # Empty list has an LIS of 0.

    # Initialize an array to store the length of LIS ending at each index.
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
    
val = lis(lst)
print(val)