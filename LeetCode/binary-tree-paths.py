# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        
        res = []
        
        self.dfs(res, [], root)
        
        s = []    
        for path in res:
            temp = ""
            for node in path:
                temp = temp + str(node) + "->"
            s.append(temp[:-2])
            
        return s
        
    def dfs(self, res, path, root):
        if root is None:
            return 
        
        path = path + [root.val]
        
        if root.left is None and root.right is None:
            res.append(path)
            return
            
        self.dfs(res, path, root.left)
        self.dfs(res, path, root.right)
        