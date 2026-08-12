# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        l, r = head, head
        c = 0
        while r:
            r = r.next
            c += 1
            if c == n:
                break
        prev = ListNode(0, head)
        head = prev
        while r:
            prev = l
            l = l.next
            r = r.next

        prev.next = l.next

        return head.next
        