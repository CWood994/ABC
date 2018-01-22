# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        
        stack = []
        
        stack.append([root,0])
        prev = None
        prev_h = 0

        while stack:
            node, level = stack.pop(0)

            if node.right:
                stack.append([node.right, level + 1])
            if node.left:
                stack.append([node.left, level + 1])
                
            if prev and prev_h == level:
                node.next = prev
            else:
                prev_h = level
            prev = node
                
                
        
            
            
        