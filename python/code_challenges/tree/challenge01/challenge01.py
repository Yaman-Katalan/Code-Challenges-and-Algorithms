# Write here the code challenge solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        TreeNode constructor to initialize a node in a binary tree.

        Args:
        - val (int): The value to be stored in the node.
        - left (TreeNode, optional): The left child node. Defaults to None.
        - right (TreeNode, optional): The right child node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    """
    Constructs a binary tree from its preorder and inorder traversal arrays.

    Args:
    - preorder (List[int]): The preorder traversal of the binary tree.
    - inorder (List[int]): The inorder traversal of the binary tree.

    Returns:
    - TreeNode: The root node of the constructed binary tree.
    """
    def buildTreeHelper(pre_start, pre_end, in_start, in_end):
        """
        Helper function to recursively construct the binary tree.

        Args:
        - pre_start (int): Start index of the current subtree in preorder.
        - pre_end (int): End index of the current subtree in preorder.
        - in_start (int): Start index of the current subtree in inorder.
        - in_end (int): End index of the current subtree in inorder.

        Returns:
        - TreeNode: The root node of the current subtree.
        """
        if pre_start > pre_end:
            return None
        
        root_val = preorder[pre_start]
        root = TreeNode(root_val)
        
        idx = inorder.index(root_val, in_start, in_end + 1)
        left_size = idx - in_start
        
        root.left = buildTreeHelper(pre_start + 1, pre_start + left_size, in_start, idx - 1)
        root.right = buildTreeHelper(pre_start + left_size + 1, pre_end, idx + 1, in_end)
        
        return root
    
    return buildTreeHelper(0, len(preorder) - 1, 0, len(inorder) - 1)



# Example 1
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = buildTree(preorder, inorder)
# The function will construct and return the binary tree structure as described.

# Example 2
preorder = [-1]
inorder = [-1]
root = buildTree(preorder, inorder)
# In this case, the root will directly be constructed since there's only one element.
