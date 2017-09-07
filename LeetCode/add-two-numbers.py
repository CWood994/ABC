# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        sum = l1.val + l2.val
        l1=l1.next
        l2=l2.next
        front = ListNode(sum%10)
        end = front
        carry = sum // 10
        while(l1 != None or l2 != None):
            v1 = 0 if l1 == None else l1.val
            v2 = 0 if l2 == None else l2.val
            sum = v1 + v2 + carry
            end.next = ListNode(sum%10)
            end = end.next
            carry = sum // 10
            l1 = None if l1 == None else l1.next
            l2 = None if l2 == None else l2.next
        
        if(carry != 0):
            end.next = ListNode(1)
            
        return front
            