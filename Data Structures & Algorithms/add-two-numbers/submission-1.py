# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        res = ListNode(0, None)
        carry = 0
        node = res

        while l1 and l2:
            sm = l1.val + l2.val + carry
            p = sm % 10
            carry = sm // 10
            res.next = ListNode(p, None)
            res = res.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sm = l1.val + carry
            p = sm % 10
            carry = sm // 10
            res.next = ListNode(p, None)
            res = res.next
            l1 = l1.next

        while l2:
            sm = l2.val + carry
            p = sm % 10
            carry = sm // 10
            res.next = ListNode(p, None)
            res = res.next
            l2 = l2.next
        
        if carry != 0:
            res.next = ListNode(carry, None)

        return node.next
