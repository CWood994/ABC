# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return head
        
        second = head
        head = head.next
        
        second.next = head.next
        head.next = second
        
        tempHead = second.next
        tempHeadPrev = second
        while tempHead is not None and tempHead.next is not None:
            secondHead = tempHead.next
            tempHeadPrev.next = secondHead
            tempHead.next = tempHead.next.next
            secondHead.next = tempHead
            tempHeadPrev = tempHead
            tempHead = tempHead.next
        
        return head
        