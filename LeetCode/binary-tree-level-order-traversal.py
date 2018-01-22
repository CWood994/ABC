# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        res = []
        self.helper(res, root)
        return res
        
    def helper(self, res, root):
        if not root:
            return
        
        queue = []
        queue.append([root,0])
        
        while queue:
            node, level = queue.pop(0)
            
            if len(res) == level:
                res.append([node.val])
            else:
                res[-1].append(node.val)
            
            if node.left:
                queue.append([node.left,level+1])
            if node.right:
                queue.append([node.right,level+1])
            
        
        
        