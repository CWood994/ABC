# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        fast_head = slow_head = head
        
        for i in range(n):
            fast_head = fast_head.next

        if fast_head is None:
            head = slow_head.next
            return head
        
        while fast_head.next is not None:
            fast_head = fast_head.next
            slow_head = slow_head.next
            
        slow_head.next = slow_head.next.next
        
        return head
        
        