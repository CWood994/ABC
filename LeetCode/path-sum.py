# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if root is None:
            return False
        
        return self.sum_left(root.right, root.left, sum-root.val)
        
        
    def sum_left(self, left, right, sum):
        left_check = right_check = False
        
        if left is not None:
            left_check =  self.sum_left(left.left, left.right, sum-left.val)
                    
        if right is not None:
            right_check =  self.sum_left(right.left, right.right, sum-right.val)
            
        if left is None and right is None and sum == 0:
            return True
            
        return left_check or right_check
            
        