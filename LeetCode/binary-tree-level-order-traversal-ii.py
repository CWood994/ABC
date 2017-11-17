# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        array = [[root.val]]

        if root.left is not None or root.right is not None:
            array.insert(0, [])
            self.appendSelfAtDepth(root.left, root.right, array, 1)

        return array

    def appendSelfAtDepth(self, left, right, array, depth):
        if len(array) < depth + 1:
            array.insert(0, [])

        my_subarray = array[-(depth + 1)]

        if right is not None:
            my_subarray.insert(0, right.val)
        if left is not None:
            my_subarray.insert(0, left.val)

        if (left is not None and (
                left.left is not None or left.right is not None)) or (
                right is not None and (
                right.left is not None or right.right is not None)):
            if right is not None:
                self.appendSelfAtDepth(right.left, right.right, array,
                                       depth + 1)
            if left is not None:
                self.appendSelfAtDepth(left.left, left.right, array, depth + 1)







