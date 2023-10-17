n, l = map(int, input().split())

# The idea here is to express n as the sum of `l` consecutive integers, and to find the
# starting integer x. To do this, we can rearrange the equation.
# n = (x+1) + (x+2) + ... + (x+l)
# n = lx + l(l+1)/2
# So, we can solve for x:
# lx = n - l(l+1)/2
# x = (n - l(l+1)/2) / l

for i in range(l, 101):
    # We start with i equal to `l` and increment it.
    
    # Calculate `x` using the formula and store it in a floating-point number.
    x = n - i * (i + 1) / 2
    
    # Check if `x` is divisible by `i`, i.e., if `x` can be an integer.
    if x % i == 0:
        x = int(x / i)  # Convert `x` to an integer.
        
        # If `x` is non-negative or -1 (meaning it contains non-negative integers),
        # print the corresponding list and break the loop.
        if x >= -1:
            print(*list(range(x + 1, x + i + 1)))
            break
else:
    # If no valid list is found in the range of l to 100, print -1.
    print(-1)
