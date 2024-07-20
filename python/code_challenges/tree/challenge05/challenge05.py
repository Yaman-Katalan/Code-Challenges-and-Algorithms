# Write here the code challenge solution
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def max_height(root):
    if not root:
        return 0
    
    queue = [root]
    height = 0
    
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.pop(0)  # Pop from the front of the list
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        height += 1
    
    return height

def build_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    index = 1
    
    while queue and index < len(values):
        node = queue.pop(0)
        
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    
    return root

# Example usage
values = [10, 20, 30, 40, 28, 27, 50, 29]
root = build_tree(values)
height = max_height(root)
print(height)  # Output: 3

