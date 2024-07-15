# Write here the code challenge solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    
    return root

from collections import deque

def printLevelOrder(root):
    if not root:
        return "[]"
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")
    
    # Trim the trailing "null" values
    while result and result[-1] == "null":
        result.pop()
    
    return result

# Test Cases
if __name__ == "__main__":
    nums1 = [0, -3, -10, 5, 9]
    tree1 = sortedArrayToBST(nums1)
    print(printLevelOrder(tree1))  # Output: [0, -3, 9, -10, "null", 5]

    nums2 = [3, 1]
    tree2 = sortedArrayToBST(nums2)
    print(printLevelOrder(tree2))  # Output: [3, 1]
