# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        return self.min_depth(root.left, root.right, 1)
        
        
    def min_depth(self, left, right, height):
        
        if left is None and right is None:
            return height
        else:
            height += 1
            if left is not None and right is not None:
                return min(self.min_depth(left.left, left.right, height), self.min_depth(right.left, right.right, height))
            elif left is not None:
                return self.min_depth(left.left, left.right, height)
            else:
                return self.min_depth(right.left, right.right, height)
        