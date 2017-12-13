# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        
        return self.check(root.left, root.right)      

    def check(self, left, right):
        if abs(self.height(left) - self.height(right)) > 1:
            return False
        
        rl = True
        if left is not None:
            rl = self.check(left.left, left.right)
            
        rr = True
        if right is not None:
            rr = self.check(right.left, right.right)
            
        return rl and rr 
        
    def height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.height(node.left), self.height(node.right))
        
        