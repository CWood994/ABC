# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        q = []
        res = []
        self.inorder(root, res)
        
        sumed = 0
        for n in res[::-1]:
            tmp = n.val
            n.val += sumed
            sumed += tmp
            
        return root
            
        
        
    def inorder(self, root, res):  
        if not root:
            return
        
        self.inorder(root.left,res)   
        res.append(root)
        self.inorder(root.right,res)
        