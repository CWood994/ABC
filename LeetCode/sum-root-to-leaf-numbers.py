# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.helper(res, [], root)
        return self.count(res)
        
    def helper(self, res, path, root):
        if not root:
            res.append(path)
            return
        
        if not root.left and not root.right:
            self.helper(res, path + [root.val], root.left)  
            return
        
        if root.left:
            self.helper(res, path + [root.val], root.left)    
        if root.right:
            self.helper(res, path + [root.val], root.right)
            
        
    def count(self, ar):
        print(ar)
        _sum = 0
        for a in ar:
            if a:
                _sum += int("".join(map(str, a)))
            
        return _sum
        
        