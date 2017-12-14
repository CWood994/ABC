# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None:
            return False
        
        head1=head
        head2=head.next
        
        while(head1 is not None and head2 is not None):
            if head1 == head2:
                return True
            head2 = self.two_step(head2)
            head1 = self.one_step(head1)
            
        return False
        
        
    def two_step(self, node):
        one = node.next
        if one is not None:
            one = one.next
            
        return one
    
    def one_step(self, node):
        return node.next
    