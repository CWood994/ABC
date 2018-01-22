# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.mergesort(head)
        
    def mergesort(self, head):
        if not head:
            return None
        if not head.next:
            return head
        
        slow = fast = head
        fast = fast.next
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        fast = slow.next
        slow.next = None
        h1 = self.mergesort(head)
        h2 = self.mergesort(fast)
        
        if h1.val < h2.val:
            head = h1
            h1=h1.next
        else:
            head = h2
            h2=h2.next
            
        cur = head
        
        
        while h1 or h2:
            if not h1:
                cur.next = h2
                h2 = h2.next
            elif not h2:
                cur.next = h1
                h1 = h1.next
            elif h1.val < h2.val:
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            cur = cur.next
            
        return head
                
        
        