import sys
input=sys.stdin.readline

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        
## root->left->right
def pre_order(node):
    print(node.value, end='')
    if node.left:
        pre_order(tree[node.left])
    if node.right:
        pre_order(tree[node.right])

def in_order(node):
    if node.left:
        in_order(tree[node.left])
    print(node.value, end='')
    if node.right:
        in_order(tree[node.right])

def post_order(node):
    if node.left:
        post_order(tree[node.left])
    if node.right:
        post_order(tree[node.right])
    print(node.value, end='')

tree = {}
n = int(input())
for i in range(n):
    n, l, r = input().split()
    if l == '.':
        l = None
    if r == '.':
        r = None
        ## not storing an actual object, but storing a reference to that object
    tree[n] = Node(n, l, r)

# Perform tree traversals starting from the root node 'A'
root_node = 'A'
pre_order(tree[root_node])
print()
in_order(tree[root_node])
print()
post_order(tree[root_node])