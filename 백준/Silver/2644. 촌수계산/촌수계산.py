from collections import defaultdict
n = int(input())
a, b = map(int, input().split())
m = int(input())

# Create an undirected graph using defaultdict(list)
graph = defaultdict(list)
for _ in range(m):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)

# Initialize visited array with False values for all nodes
visited = [False] * (n + 1)

def dfs(node, depth):
    # Mark the current node as visited
    visited[node] = True

    # Base case: If the target node is found, return the current depth
    if node == b:
        return depth

    # Explore unvisited child nodes
    for child in graph[node]:
        if not visited[child]:
            # Recursively search for the target node through the child
            result = dfs(child, depth + 1)

            # If the target node is found in a child subtree, return the depth
            if result != -1:
                return result

    # If the target node is not found in any child subtree, return -1
    return -1

# Start the DFS from node a with depth 0
shortest_path_depth = dfs(a, 0)

# Print the shortest path length if found, otherwise -1
print(shortest_path_depth if shortest_path_depth != -1 else -1)