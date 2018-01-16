# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        
        slow = head
        fast = head.next.next
        
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            
        tmp = slow.next
        root = TreeNode(tmp.val)
        root.right = self.sortedListToBST(tmp.next)
        slow.next = None
        root.left = self.sortedListToBST(head)
        
        return root
        