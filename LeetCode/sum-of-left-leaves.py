# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        return self.isLeft(root.left) + self.sumOfLeftLeaves(root.right)
        
    def isLeft(self, root):
        if root is None:
            return 0
        
        if root.left == None and root.right == None:
            return root.val
        
        return self.isLeft(root.left) + self.sumOfLeftLeaves(root.right)    
        
        
        