# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None:
            return True
        
        return self.helper(root, None, None)
    
    def helper(self, root, _min, _max):
        print(_min, _max)
        if root is None:
            return True
        
        if (_min is not None and root.val <= _min) or (_max is not None and root.val >= _max):
            print("FAILED")
            return False

        l=r=True

        if root.right:
            r = self.helper(root.right, root.val , _max)
        if root.left:
            if _max is None:
                _max = root.val
            l = self.helper(root.left, _min , min(_max, root.val))

            
        return l and r
                