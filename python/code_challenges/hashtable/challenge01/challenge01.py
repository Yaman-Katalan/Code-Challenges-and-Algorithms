# Write here the code challenge solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_target(root, k):
    def inorder(node):
        if not node:
            return False
        if inorder(node.left):
            return True
        complement = k - node.val
        if complement in seen:
            return True
        seen.add(node.val)
        return inorder(node.right)
    
    seen = set()
    return inorder(root)

    
# Example usage:
# Creating the BST [7,2,9,1,5,null,14]
root = TreeNode(7)
root.left = TreeNode(2)
root.right = TreeNode(9)
root.left.left = TreeNode(1)
root.left.right = TreeNode(5)
root.right.right = TreeNode(14)

k1 = 3
k2 = 4

print(find_target(root, k1))  # Output: True
print(find_target(root, k2))  # Output: True
