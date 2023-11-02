n, m = map(int, input().split())
leaf = 0

# If there are only 2 nodes, consider one of them as a leaf
if m == 2:
    leaf = 1

last_leaf = 0

# Iterate through the nodes from 1 to n-1
for i in range(1, n):
    if m > leaf:
        # If there is a need for more leaf nodes, connect the current node to node i
        print(0, i)
        leaf += 1
    else:
        # If there are enough leaf nodes, connect the current node to the last leaf node
        print(last_leaf, i)
    
    last_leaf = i  # Update the last connected leaf node