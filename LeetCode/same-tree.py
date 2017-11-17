# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        left = True
        if p.left is not None or q.left is not None:
            left = False
        if p.left is not None and q.left is not None:
            left = self.isSameTree(p.left, q.left)

        right = True
        if p.right is not None or q.right is not None:
            right = False
        if p.right is not None and q.right is not None:
            right = self.isSameTree(p.right, q.right)

        return right and left
