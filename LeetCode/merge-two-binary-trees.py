class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        return self.merge(t1, t2)
        
    def merge(self, t1, t2):
        if not t1 and not t2:
            return None
        if not t1:
            return self.dup(t2)
        if not t2:
            return self.dup(t1)
        
        v1 = t1.val if t1 else 0
        v2 = t2.val if t2 else 0
        
        root = TreeNode(v1 + v2)
        root.left = self.merge(t1.left, t2.left)
        root.right = self.merge(t1.right, t2.right)
        return root
    
    def dup(self, t):
        if not t:
            return None
        
        root = TreeNode(t.val)
        root.left = self.dup(t.left)
        root.right = self.dup(t.right)
        return root
        
        
        
        