# Write here the code challenge solution

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_node(root.left, value)
    else:
        root.right = insert_node(root.right, value)
    return root

def find_max_inorder(root):
    max_value = float('-inf')
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        if current.value > max_value:
            max_value = current.value

        current = current.right

    return max_value

# Helper function to build a tree from a list
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    for value in values[1:]:
        insert_node(root, value)
    return root

# Example usage:
values = [1000, 500, 2000, 250, 600, 12000]
root = build_tree(values)
max_value = find_max_inorder(root)
print("Maximum value in the tree is:", max_value)
