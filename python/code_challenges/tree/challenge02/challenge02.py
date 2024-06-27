# Write here the code challenge solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initialize a binary tree node.

        Parameters:
        val (int): Value of the node.
        left (TreeNode): Left child of the node.
        right (TreeNode): Right child of the node.
        """
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    """
    Check if two binary trees are the same using breadth-first traversal.

    Parameters:
    p (TreeNode): Root node of the first binary tree.
    q (TreeNode): Root node of the second binary tree.

    Returns:
    bool: True if both trees are the same, False otherwise.
    """
    # Create two lists for Breadth-First Traversal
    queue1 = [p]
    queue2 = [q]
    
    while queue1 and queue2:
        node1 = queue1.pop(0)
        node2 = queue2.pop(0)
        
        if not node1 and not node2:
            continue
        
        if not node1 or not node2:
            return False
        
        if node1.val != node2.val:
            return False
        
        queue1.append(node1.left)
        queue1.append(node1.right)
        
        queue2.append(node2.left)
        queue2.append(node2.right)
    
    return not queue1 and not queue2

# Example usage:
# Tree 1: [1,2,3]
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

# Tree 2: [1,2,3]
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(isSameTree(p, q))  # Output: True
